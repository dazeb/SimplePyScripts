#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import json

# pip install dpath
import dpath.util

from bs4 import BeautifulSoup

from common import session, URL_BASE, Game


def get_game_info(game_id: int) -> Game:
    url = f"{URL_BASE}/game/{game_id}"

    rs = session.get(url)
    rs.raise_for_status()

    soup = BeautifulSoup(rs.content, "html.parser")

    next_data_el = soup.select_one("#__NEXT_DATA__")
    if not next_data_el:
        raise Exception('Not found id="__NEXT_DATA__"!')

    next_data_str = next_data_el.string

    next_data = json.loads(next_data_str)
    return Game.parse(
        data=dpath.util.get(next_data, "**/data/game/0")
    )


if __name__ == "__main__":
    print(
        get_game_info(game_id=3505)
    )
    # Game(id=3505, title='Final Fantasy IX', aliases=['Final Fantasy 9', 'FF9'], duration_main_seconds=138721, duration_main_title='38:32:01', duration_plus_seconds=189924, duration_plus_title='52:45:24', duration_100_seconds=299502, duration_100_title='83:11:42', duration_all_seconds=171503, duration_all_title='47:38:23', release_world='2000-02-16', profile_platforms=['Mobile', 'Nintendo Switch', 'PC', 'PlayStation', 'PlayStation 4', 'Xbox One'], profile_genres=['Role-Playing'])

    print(
        get_game_info(game_id=3519)
    )
    # Game(id=3519, title='Final Fantasy VI', aliases=['Final Fantasy III [NA]', 'Final Fantasy 3 [NA]', 'Final Fantasy 6', 'FF6', 'Final Fantasy VI Advance', 'Final Fantasy VI: Pixel Remaster'], duration_main_seconds=124906, duration_main_title='34:41:46', duration_plus_seconds=147288, duration_plus_title='40:54:48', duration_100_seconds=220653, duration_100_title='61:17:33', duration_all_seconds=148583, duration_all_title='41:16:23', release_world='1994-04-02', profile_platforms=['Game Boy Advance', 'Mobile', 'Nintendo Switch', 'PC', 'PlayStation', 'PlayStation 4', 'Super Nintendo'], profile_genres=['Turn-Based', 'Role-Playing'])
