#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import re
from bs4 import BeautifulSoup
from common import session


def get_notes(url: str) -> list[str]:
    rs = session.get(url)
    rs.raise_for_status()

    items = []

    soup = BeautifulSoup(rs.content, "html.parser")

    # NOTE: Example
    # <ol class="references">
    #     <li id="190cite_note-34548627613">
    #         <a href="#190cite_ref-34548627613">↑</a> Автор тут допустил небольшую ошибку. Циклотетраметилентетранитрамин ещё называют октогеном, но не СL-20. СL-20 будет «гексанитрогексаазаизовюрцитан», он более эффективен и стоит 1300 долларов за килограмм, октоген же — 100 долларов за килограмм.
    #     </li>
    # </ol>
    for li_el in soup.find_all("li", id=re.compile(".*note.*")):
        if li_el.a:
            li_el.a.decompose()
        items.append(
            li_el.get_text(strip=True)
        )

    return items


if __name__ == "__main__":
    url = "https://ranobehub.org/ranobe/19/17/4"
    notes = get_notes(url)
    print(f"Notes ({len(notes)}):")
    for note in notes:
        print(repr(note))
    """
    Notes (3):
    'Автор тут допустил небольшую ошибку. Циклотетраметилентетранитрамин ещё называют октогеном, но не СL-20. СL-20 будет «гексанитрогексаазаизовюрцитан», он более эффективен и стоит 1300 долларов за килограмм, октоген же — 100 долларов за килограмм.'
    'В предыдущих томах её фамилия была Баранс.'
    'Канопус: звезда южного полушария, вторая по яркости после Сириуса.'
    """

    print()

    url = "https://ranobehub.org/ranobe/19/21/2"
    notes = get_notes(url)
    print(f"Notes ({len(notes)}):")
    for note in notes:
        print(repr(note))
    """
    'Примечание переводчика: я сейчас активно изучаю японский язык, и мне всё меньше нравятся неправильные имена, названия и тому подобное. Поэтому некоторые из имён и фамилий я переведу на систему Поливанова, а старые устоявшиеся термины заменю на нормальные. Обо всех изменениях будет указано в подобных примечаниях: стар. Азуса.'
    'Стар. Изуми.'
    'Стар. Йошида.'
    'Стар. Мизуки.'
    'Стар. Оогуро Рууя.'
    'Стар. USNA.'
    'Стар. Сильвия Меркурий Первая.'
    'Стар. Катсуто.'
    """
    print()

    url = "https://ranobehub.org/ranobe/19/202/2"
    notes = get_notes(url)
    print(f"Notes ({len(notes)}):")
    for note in notes:
        print(repr(note))
    """
    'VTOL(СВВП) — Самолет Вертикального Взлета и Посадки.'
    'Тёфу — городок к западу от Токио.'
    'Одати — длинный меч с длиной клинка не менее 90 см (обычно 130-180).'
    'Вакидзаси — короткий меч с длиной клинка от 30 до 60 см.'
    'Поза "Сэйдза", она же известна как "по-японски" — "правильная" поза для сидения: на коленях, пятки сомкнуты сзади и направлены вверх, и ягодицы усажены на эти пятки.'
    'Эрика говорит сокращенно "PK" — ПсихоКинез. Психокинез это американский аналог слова телекинез, которое у нас более популярно.'
    '[Front Double Biceps][Front Lat Spread][Most muscular] Названия поз у автора написаны на английском, я привел русские варианты, взятые из википедии. Если кому интересно, как это выглядит, то и по русскому и по английскому названию легко гуглятся картинки.'
    'АС — Абсолютное Смазывание, уникальная магия Аяко, см. том 13, главу 5'
    """