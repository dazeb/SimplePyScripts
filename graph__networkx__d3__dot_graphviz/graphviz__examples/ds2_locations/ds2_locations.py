#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


# pip install graphviz
from graphviz import Graph


def get_graph():
    g = Graph("g", filename="ds2_locations.gv", comment="Locations Dark Souls")

    # SOURCE: https://github.com/gil9red/SimplePyScripts/blob/45852f0541644dfb0478e98e2df530c1bb93eeae/Dark%20Souls/generate_HTML_location_graph__with_d3js/generate_graph_html__Dark_Souls.py
    links = [
        ("Алтарь Огня", "Бездна"),
        ("Алтарь Огня", "Горнило Первого Пламени"),
        ("Алтарь Огня", "Храм Огня"),
        ("Алтарь Света", "Город Нежити"),
        ("Алтарь Света", "Уезд Нежити"),
        ("Анор Лондо", "Архивы Герцога"),
        ("Анор Лондо", "Крепость Сена"),
        ("Анор Лондо", "Нарисованный Мир Ариамис"),
        ("Архивы Герцога", "Кристальный Грот"),
        ("Бездна", "Руины Нового Лондо"),
        ("Владение Квилег", "Руины Демонов"),
        ("Владение Квилег", "Чумной Город"),
        ("Глубины", "Город Нежити"),
        ("Глубины", "Чумной Город"),
        ("Город Нежити", "Озеро Темных Корней"),
        ("Город Нежити", "Уезд Нежити"),
        ("Город Нежити", "Храм Огня"),
        ("Долина Драконов", "Озеро Темных Корней"),
        ("Долина Драконов", "Руины Нового Лондо"),
        ("Долина Драконов", "Чумной Город"),
        ("Забытый Изалит", "Руины Демонов"),
        ("Зал Стоицизма", "Поселок Олачиль"),
        ("Катакомбы", "Склеп Великанов"),
        ("Катакомбы", "Храм Огня"),
        ("Королевский Лес", "Поселок Олачиль"),
        ("Королевский Лес", "Святилище Олачиля"),
        ("Королевский Лес", "Ущелье Бездны"),
        ("Крепость Сена", "Уезд Нежити"),
        ("Озеро Золы", "Полость"),
        ("Озеро Темных Корней", "Сад Темных Корней"),
        ("Озеро Темных Корней", "Священный Сад"),
        ("Подземелье Поселка Олачиль", "Поселок Олачиль"),
        ("Подземелье Поселка Олачиль", "Ущелье Бездны"),
        ("Полость", "Чумной Город"),
        ("Поселок Олачиль", "Битва За Стоицизм"),
        ("Руины Нового Лондо", "Храм Огня"),
        ("Сад Темных Корней", "Уезд Нежити"),
        ("Святилище Олачиля", "Священный Сад"),
        ("Северное Прибежище Нежити", "Храм Огня"),
        ("Уезд Нежити", "Глубины"),
        ("Уезд Нежити", "Храм Огня"),
    ]

    for a, b in links:
        g.edge(a, b)

    g.attr(label=r"\n\nLocations Dark Souls")
    return g


if __name__ == "__main__":
    g = get_graph()
    g.view()

    # g.render(format='jpg')
