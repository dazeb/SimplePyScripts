#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import pathlib

# pip install humanize
from humanize import naturalsize as sizeof_fmt


def get_dir_total_size(dir_name: str) -> tuple[int, str]:
    total_size = 0

    for file_name in pathlib.Path(dir_name).glob("**/*"):
        if file_name.is_file():
            total_size += file_name.stat().st_size

    return total_size, sizeof_fmt(total_size)


if __name__ == "__main__":
    import os

    # paths = [r"C:\Users\Default", r"C:\Program Files (x86)", os.path.expanduser(r'~\Desktop')]
    paths = [".."]

    for path in paths:
        path = os.path.abspath(path)

        size, size_str = get_dir_total_size(path)
        print(f'"{path}": {size} bytes / {size_str}')
