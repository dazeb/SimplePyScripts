#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import time

from datetime import datetime
from pathlib import Path
from typing import Type

# pip install peewee
from peewee import SqliteDatabase, Model, TextField, CharField, DateTimeField

from get_wish_info import Wish as WishInfo
from get_last_id_wish import get_last_id_wish


DIR = Path(__file__).resolve().parent


db = SqliteDatabase(DIR / "dump.sqlite")


class BaseModel(Model):
    class Meta:
        database = db

    @classmethod
    def get_inherited_models(cls) -> list[Type["BaseModel"]]:
        return sorted(cls.__subclasses__(), key=lambda x: x.__name__)

    @classmethod
    def print_count_of_tables(cls):
        items = []
        for sub_cls in cls.get_inherited_models():
            name = sub_cls.__name__
            count = sub_cls.select().count()
            items.append(f"{name}: {count}")

        print(", ".join(items))

    def __str__(self):
        fields = []
        for k, field in self._meta.fields.items():
            v = getattr(self, k)

            if isinstance(field, (TextField, CharField)):
                v = repr(v)

            fields.append(f"{k}={v}")

        return self.__class__.__name__ + "(" + ", ".join(fields) + ")"


class Wish(BaseModel):
    user = TextField()
    user_url = TextField()
    title = TextField()
    created_at = DateTimeField()
    img_url = TextField()


db.connect()
db.create_tables(BaseModel.get_inherited_models())


def run():
    wish_id = 1
    last_id_wish = get_last_id_wish()

    current_last_id = Wish.select(Wish.id).order_by(Wish.id.desc()).scalar()
    if current_last_id:
        wish_id = current_last_id + 1

    while wish_id < last_id_wish:
        print(f"#{wish_id}")

        try:
            wish_info = WishInfo.parse_from(wish_id)
            if wish_info:
                wish_data = wish_info.as_dict()
                wish_data["created_at"] = datetime.strptime(
                    wish_data["created_at"], "%Y-%m-%d %H:%M"
                )
                Wish.create(**wish_data)
            else:
                print(f"#{wish_id} не найдено!")

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)
            continue

        wish_id += 1
        time.sleep(0.050)

        # Достигли максимального известного id - попробуем его обновить
        if wish_id == last_id_wish:
            last_id_wish = get_last_id_wish()


if __name__ == "__main__":
    run()