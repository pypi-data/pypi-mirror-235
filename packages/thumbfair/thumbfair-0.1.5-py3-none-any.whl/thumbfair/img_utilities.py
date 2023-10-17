from PIL.ImageFont import FreeTypeFont
from PIL.Image import Image as ImageType

from PIL import Image, ImageDraw
from PIL.Image import Image as ImageType


def fade_out_img(im: ImageType, start: float = 0.80) -> ImageType:
    """Create a fade-out effect on the edge of the image. Translate the
    image and re-translate it after the fade-out to apply it to the left
    edge.

    Idea originally from StackOverflow, modified by me.
    """

    width, height = im.size
    pixels = im.load()

    for x in range(int(width * start), width):
        for y in range(height):
            alpha = pixels[x, y][3] - int((x - width * start) / width / 0.20 * 255)

            # if alpha <= 0: alpha = 0
            alpha = max(0, alpha)

            pixels[x, y] = pixels[x, y][:3] + (alpha,)

    for x in range(x, width):  # type: ignore
        for y in range(height):
            pixels[x, y] = pixels[x, y][:3] + (0,)

    return im


def gen_gradient_bordered_text(
    text: str,
    border_color: str,
    border_px: int,
    grad_dir: str,
    font: FreeTypeFont,
) -> ImageType:
    """
    Mixes solutions from:
        https://stackoverflow.com/questions/14211340
        https://stackoverflow.com/questions/63246100
        https://stackoverflow.com/questions/41556771
    to create a string of text that has both a gradient and a border.
    """

    # todo: separate into two separate scripts

    # size of canvas, which will be cropped to the absolute minimum before returning
    w, h = (1280, 120)

    # load and resize gradient img (note that final size influences gradient)
    grad_img = Image.open(grad_dir).resize((w, h))

    # create new black alpha channel used to draw the text and put a gradient background
    alpha = Image.new("L", (w, h), "black")
    draw = ImageDraw.Draw(alpha)

    # create an additional layer to draw the border/contour/edge of the text
    edge_layer = Image.new("RGBA", (w, h))
    edge_draw = ImageDraw.Draw(edge_layer)

    # create border using the specified thickness
    edge_draw.text((20 - border_px, 20 - border_px), text, font=font, fill=border_color)
    edge_draw.text((20 + border_px, 20 - border_px), text, font=font, fill=border_color)
    edge_draw.text((20 - border_px, 20 + border_px), text, font=font, fill=border_color)
    edge_draw.text((20 + border_px, 20 + border_px), text, font=font, fill=border_color)

    # draw the actual text in white to replace it later
    # padding is used to avoid cropping of letters
    draw.text((15, 15), text, fill="white", font=font)

    # use text cutout as alpha channel for gradient image
    grad_img.putalpha(alpha)

    # crop extra alpha
    grad_img = grad_img.crop(grad_img.getbbox())
    edge_layer = edge_layer.crop(edge_layer.getbbox())

    # paste gradient text over contoured text
    edge_layer.paste(grad_img, (5, 5), grad_img)

    return edge_layer
