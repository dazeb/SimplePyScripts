#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import datetime as dt

# pip install psutil
import psutil


for proc in psutil.process_iter():
    if not proc.name().startswith("python"):
        continue

    secs = proc.create_time()
    started = dt.datetime.fromtimestamp(secs)
    if (dt.datetime.now() - started) >= dt.timedelta(hours=1):
        print(proc)
