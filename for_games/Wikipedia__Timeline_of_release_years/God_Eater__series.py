#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


# Хронология выхода игр


from common import get_parsed_two_column_wikitable


def is_match_table_func(table) -> bool:
    return "TIMELINE OF RELEASE YEARS" in table.caption.text.strip().upper()


url = "https://en.wikipedia.org/wiki/God_Eater"
for year, name in get_parsed_two_column_wikitable(url, is_match_table_func):
    print(f"{year}: {name}")

# 2010: God Eater
# 2010: Gods Eater Burst
# 2010: God Eater Mobile
# 2013: God Eater 2
# 2014: God Eater 2 Rage Burst
# 2015: God Eater Resurrection
# 2017: God Eater Online
# 2018: God Eater Resonant Ops
# 2018: God Eater 3
