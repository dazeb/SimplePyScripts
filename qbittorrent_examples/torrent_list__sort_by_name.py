#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


# SOURCE: https://github.com/qbittorrent/qbittorrent/wiki/WebUI-API-Documentation#get-torrent-list


from common import get_client, print_torrents


qb = get_client()

torrents = qb.torrents(sort="name")

# Desc / Reverse:
# torrents = qb.torrents(sort='name', reverse='true')

print_torrents(torrents)
