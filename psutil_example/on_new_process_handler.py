#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


from threading import Thread
from time import sleep
from typing import Callable

# pip install psutil
import psutil


ListenerFunc = Callable[[list], None]


class OnNewProcessHandler(Thread):
    def __init__(self, timeout_secs=1.0):
        super().__init__()

        self._process = dict()
        self._listeners: list[ListenerFunc] = []
        self._timeout_secs = timeout_secs

    def add_listener(self, listener: ListenerFunc):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def remove_listener(self, listener: ListenerFunc):
        if listener in self._listeners:
            self._listeners.remove(listener)

    def remove_all_listener(self):
        self._listeners.clear()

    @staticmethod
    def get_process() -> dict:
        items = dict()

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=["pid", "name", "exe"])
                items[pinfo["pid"]] = pinfo

            except psutil.NoSuchProcess:
                continue

        return items

    def run(self):
        while True:
            current_process = self.get_process()

            # При первом запуске не оповещаем
            if not self._process:
                self._process.clear()
                self._process.update(current_process)
                continue

            diff_pids = set(current_process.keys()) - set(self._process.keys())
            if diff_pids:
                self._process.clear()
                self._process.update(current_process)

                for l in self._listeners:
                    l([self._process[k] for k in diff_pids])

            sleep(self._timeout_secs)


if __name__ == "__main__":

    def print_listener(process_list):
        result = []
        for p in process_list:
            result.append(f"{p['name']} (pid={p['pid']})")

        print("-" * 10 + "\n" + "\n".join(result) + "\n" + "-" * 10)

    handler = OnNewProcessHandler()
    handler.add_listener(print_listener)
    handler.start()

    sleep(2)
    handler.add_listener(lambda x: print(f"New process: {len(x)}"))
