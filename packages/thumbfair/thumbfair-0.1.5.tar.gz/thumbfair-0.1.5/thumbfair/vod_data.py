from dataclasses import dataclass
import re
import sys
from pytube import Playlist, YouTube
import json


@dataclass
class VodData:
    tournament_name: str
    round_name: str
    player1: str
    char1: str
    skin1: str
    player2: str
    char2: str
    skin2: str


def playlist_to_titles(url: str) -> tuple:
    """For every video in the playlist, append its title to a list and return it."""
    p = Playlist(url)
    titles = []

    for vid_url in p:
        yt_vid = YouTube(vid_url)
        titles.append(yt_vid.title)

    return titles, p.title


def title_to_vod_data(title: str) -> VodData:
    """Parses a vod title to find every field needed to instantiate a VodData object."""

    vod_fields = []
    patterns = [
        r"\| ([\w*\s-]*) \-",  # | <round_name> -
        r"\- ([\w*\s*\'*.*]+) \(",  # - <nickname1> (
        r"\(([\w*\s*.*\&*]*)[\w*\s*.*\&*\,]*\) vs",  # (<character1>) vs
        r"vs ([\w*\s*\'*.*]*) \(",  # vs <nickname2> (
        r"vs [\w*\s*\'*]* \(([\w*\s*.*\&*]*)[\w*\s*.*\&*\,]*\)",  # vs <nickname2> (<character2>)
    ]

    # finds every part of the title and adds it to a list
    for p in patterns:
        current_re = re.search(p, title)
        if current_re:
            vod_fields.append(current_re.group(1))
        else:
            vod_fields.append("")

    # easier to just split and prepend for this one
    tournament_name = title.split("|")[0].strip()
    vod_fields.insert(0, tournament_name)

    # gets the character skin for each player from a json
    with open(f"resources/skins.json", encoding="utf8") as skins_json:
        skins = json.load(skins_json)

    p1_nick = vod_fields[2]
    p2_nick = vod_fields[4]

    p1_skin = skins[vod_fields[3]].get(p1_nick, 1)
    p2_skin = skins[vod_fields[5]].get(p2_nick, 1)

    vod_fields.insert(4, p1_skin)
    vod_fields.insert(7, p2_skin)

    # logging.info(f'Vod succesfully processed:{VodData(*vod_fields)}')

    # returns a VodData object
    return VodData(*vod_fields)


def fetch_vod_data(location: str, mode: str) -> tuple:
    # define initial vod_data as empty list, initial title as empty string
    vod_data = []

    # fetch set data from playlist
    if mode == "playlist":
        titles_list, title = playlist_to_titles(location)
        vod_data = [title_to_vod_data(t) for t in titles_list]
    # fetch set data from timestamps file
    else:
        with open(location, encoding="utf-8") as vods:
            f = vods.readlines()
            vod_data = [title_to_vod_data(t) for t in f]
            title = vod_data[0].tournament_name

    # aliases to replace problematic nicknames with (only necessary if using timestamps file)
    aliases = {}

    # replace nickname with aliases
    for v in vod_data:
        for nick, alias in aliases.items():
            v.player1 = v.player1.replace(nick, alias)
            v.player2 = v.player2.replace(nick, alias)

    return vod_data, title
