import logging
import logging.config
import os
from typing import Dict
from dotenv import load_dotenv

from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as ImageType
from PIL.Image import Transpose
import yaml

from .img_utilities import fade_out_img, gen_gradient_bordered_text
from .offsets_amsz import (
    char_offsets,
    char_resizal,
    default_char_1_offset_x,
    default_char_1_offset_y,
    default_char_2_offset_y,
    round_offset,
)
from .vod_data import VodData, fetch_vod_data


def setup_logging(path: str = "logging.yaml", level=logging.INFO) -> None:
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=level)


def build_characters_layer(chars_dir: str, data: VodData) -> ImageType:
    # load the selected characters
    p1_char = Image.open(f"{chars_dir}/{data.char1}/{data.skin1}.png").convert("RGBA")
    p2_char = Image.open(f"{chars_dir}/{data.char2}/{data.skin2}.png").convert("RGBA")

    p1_char_layer = Image.new("RGBA", (680, 720))
    p2_char_layer = Image.new("RGBA", (680, 720))

    # resizes char images to fit each box
    resize_factor_p1 = char_resizal.get(data.char1, 0.80)
    resize_factor_p2 = char_resizal.get(data.char2, 0.80)

    p1_char = p1_char.resize(tuple(int(t * resize_factor_p1) for t in p1_char.size))  # type: ignore
    p2_char = p2_char.resize(tuple(int(t * resize_factor_p2) for t in p2_char.size))  # type: ignore

    # load character offset from dictionary (return some default value if offset not present)
    offset_p1 = char_offsets.get(data.char1, (0, 0))
    offset_p2 = char_offsets.get(data.char2, (0, 0))

    # general character layers, holding every character
    chars_layer = Image.new("RGBA", (1280, 720))

    # paste chars onto layer
    p1_char_layer.paste(
        p1_char,
        (
            -350 + default_char_1_offset_x + offset_p1[0],
            default_char_1_offset_y + offset_p1[1],
        ),
    )
    p2_char_layer.paste(
        p2_char,
        (
            -350 + offset_p2[0],
            default_char_2_offset_y + offset_p2[1],
        ),
        p2_char,
    )

    p1_char_layer = fade_out_img(p1_char_layer)
    p2_char_layer = fade_out_img(
        p2_char_layer.transpose(Transpose.FLIP_LEFT_RIGHT)
    ).transpose(Transpose.FLIP_LEFT_RIGHT)

    chars_layer.paste(p1_char_layer, (0, 0), p1_char_layer)
    chars_layer.paste(p2_char_layer, (680, 0), p2_char_layer)

    return chars_layer


def build_text_layer(data: VodData, fonts_dir: str, config: Dict):
    # setting up fonts
    nicknames_font = ImageFont.truetype(
        f"{fonts_dir}/{config['nicknames_font']}", config["nicknames_size"]
    )
    round_font = ImageFont.truetype(
        f"{fonts_dir}/{config['round_font']}", config["round_size"]
    )
    # title_font = ImageFont.truetype(
    #     f"{fonts_dir}/{config['title_font']}", config["title_size"]
    # )

    # draw text (nicknames, round and tournament name)
    text_layer = Image.new("RGBA", (1280, 720))
    draw = ImageDraw.Draw(text_layer)

    # draw players nicknames
    nickname1_img = gen_gradient_bordered_text(
        data.player1,
        border_color="#000000",
        border_px=4,
        grad_dir=r"resources/layers/gradient.png",
        font=nicknames_font,
    )
    nickname2_img = gen_gradient_bordered_text(
        data.player2,
        border_color="#000000",
        border_px=4,
        grad_dir=r"resources/layers/gradient.png",
        font=nicknames_font,
    )

    # paste nicknames in the center of each nick area
    nickname_area_W = 535
    nickname_area_Y = 535
    text_layer.paste(
        nickname1_img,
        ((nickname_area_W - nickname1_img.size[0]) // 2, nickname_area_Y),
        # nickname1_img,
    )
    text_layer.paste(
        nickname2_img,
        (750 + (nickname_area_W - nickname2_img.size[0]) // 2, nickname_area_Y),
        # nickname2_img,
    )

    # draw round text
    draw.text(
        round_offset,
        data.round_name,
        "#000000",
        font=round_font,
        anchor="mm",
    )

    # text_layer.show()

    return text_layer


def gen_thumbnail(layers: list, data: VodData, config: Dict) -> Image.Image:
    """Takes a VodData object as a parameter and generates a thumbnail image, returning an Image."""

    # resources directories
    layers_dir, fonts_dir, chars_dir = (
        "./resources/layers",
        "./resources/fonts",
        str(os.getenv("portraits_dir")),
    )

    # generate and return characters layer
    chars_layer = build_characters_layer(chars_dir, data)

    # generate and return text layer
    text_layer = build_text_layer(data, fonts_dir, config)

    # create new output Image object
    output = Image.new("RGBA", (1280, 720))

    # logic for layers-based thumbnail construction
    for i, l in enumerate(layers):
        # get the next layer to be processed: it can be either a "dynamic" layer
        # (i.e., a runtime-generated layer) or a static one, loaded from a file.
        next_layer = layers[i]

        # "if"s process dynamic layers; "else" processes static layers
        if l == "text":
            next_layer = text_layer
        elif l == "renders":
            next_layer = chars_layer
        else:
            next_layer = Image.open(f"{layers_dir}/{l}").convert("RGBA")

        # paste layer onto current output
        output = Image.alpha_composite(output, next_layer)

    return output


def gen_thumbnail_for_vod(location: str, source: str) -> None:
    """
    Utility function to generate thumbnails from a timestamps file or from a playlist.
    Parameter location is supposed to be a url, while source can be either
    "timestamps" or "playlist".
    """

    load_dotenv()
    setup_logging()

    # return a VodData object from the chosen location
    # valid modes are 'playlist' or 'timestamps'
    vod_data, title = fetch_vod_data(location, source)

    print(title)

    logging.info(f"Succesfully fetched vod data for vod {title}.")

    # layers order
    layers = [
        "background.png",
        "renders",
        "banner_partealta_partebassa.png",
        "cartelli_vs.png",
        "text",
        "logo.png",
    ]

    # generate thumbnail for each set
    for data in vod_data:
        data.tournament_name = "".join(filter(str.isdigit, data.tournament_name))
        data.char1 = data.char1.replace(".", "")
        data.char2 = data.char2.replace(".", "")

        # convert to uppercase to fit the style of the graphic
        data.player1 = data.player1.upper()
        data.player2 = data.player2.upper()
        data.round_name = data.round_name.upper()

        # generate thumbnail using vod data, background and foreground
        thumbnail = gen_thumbnail(
            layers,
            data,
            {
                "layers": layers,
                "nicknames_font": "Brush-King.otf",
                "nicknames_size": 45,
                "round_font": "aAbsoluteEmpire.ttf",
                "round_size": 45,
            },
        )

        if not os.path.exists(f"./output/{title}/"):
            logging.warning(
                f'Directory {f"./output/{title} does not exist; creating it"}'
            )
            os.mkdir(f"./output/{title}/")

        # save thumbnail to output directory
        thumbnail_dir = f"./output/{title}/{data.player1.lower()}_{data.player2.lower()}_{data.round_name.lower()}.png"
        thumbnail.save(thumbnail_dir)

        logging.info(
            f"Thumbnail succesfully created: \"{thumbnail_dir.split('/')[-1]}\""
        )


if __name__ == "__main__":
    # location = "https://www.youtube.com/playlist?list=PL4UuyXCR5_jzgCV-a391CbCqaSd9MhZe9"
    # location = "https://www.youtube.com/playlist?list=PL4UuyXCR5_jwI9BUZdY12l4i9NjY3ogG5"
    # location = "https://www.youtube.com/playlist?list=PL4UuyXCR5_jwjS7Wp1zBjRqkormTP2vJo"
    # location = "https://www.youtube.com/playlist?list=PL4UuyXCR5_jwGWpIOJHI-3NFPLEPvYdxB"
    # location = 'https://www.youtube.com/playlist?list=PL4UuyXCR5_jxBf7CT0s0tlW4BbOdF-BwZ'
    # location = 'https://www.youtube.com/playlist?list=PL4UuyXCR5_jz8Pt8J1bJUTj73c0u1iZhn'
    # location = 'https://www.youtube.com/playlist?list=PL4UuyXCR5_jwuPdBiRbL_K1rvxSJb-XC1'
    # location = 'https://www.youtube.com/playlist?list=PLucm-mU6P858IbFzfmrIdi1JH-Bn7q3MM'
    # location = 'https://www.youtube.com/playlist?list=PLucm-mU6P85_cuz1ejO8X_Tffwga-z-CG'
    # location = 'https://www.youtube.com/playlist?list=PLucm-mU6P85_fw8gw3rZSlUy3ewbn2Ai2'
    # location = "https://www.youtube.com/playlist?list=PLucm-mU6P8587RwQbix5iAsjJ2CErXj0P"
    # location = "https://www.youtube.com/playlist?list=PLucm-mU6P859wntcIaanfvrqiR6svTh1h"
    location = "AMSZ3.md"

    gen_thumbnail_for_vod(location, "timestamps")
