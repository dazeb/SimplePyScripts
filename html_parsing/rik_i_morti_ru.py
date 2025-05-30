#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_season_by_series() -> dict[str, list[str]]:
    url = "http://rik-i-morti.ru/"

    s = requests.session()
    s.headers[
        "User-Agent"
    ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"

    rs = s.get(url)
    rs.raise_for_status()

    soup = BeautifulSoup(rs.content, "html.parser")

    season_by_series: dict[str, list[str]] = dict()

    for cell in soup.select(".alltable > .cell"):
        title = cell.p.get_text(strip=True)
        season_url = urljoin(rs.url, cell.a["href"])

        rs_season = s.get(season_url)
        rs_season.raise_for_status()

        soup = BeautifulSoup(rs_season.content, "html.parser")
        season_by_series[title] = [
            x.get_text(strip=True)
            for x in soup.select(".short-item > .short-head > h3 > a")
        ]

        # Не нужно напрягать сайт
        time.sleep(1)

    return season_by_series


if __name__ == "__main__":
    season_by_series = get_season_by_series()
    print("Total seasons:", len(season_by_series))
    print("Total episodes:", sum(map(len, season_by_series.values())))
    # Total seasons: 7
    # Total episodes: 71

    print()

    for season, episodes in season_by_series.items():
        print(season)

        for episode in episodes:
            print(episode)

        print()
    """
    Сезон 1
    1 сезон 1 серия: Пилотный эпизод
    1 сезон 2 серия: Пёс-газонокосильщик
    1 сезон 3 серия: Анатомический парк
    1 сезон 4 серия: М. Найт Шьямал-Инопланетяне!
    1 сезон 5 серия: Мисикс и разрушение
    1 сезон 6 серия: Вакцина Рика #9
    1 сезон 7 серия: Взрослеющий газорпазорп
    1 сезон 8 серия: Рикдцать минут
    1 сезон 9 серия: Надвигается нечто риканутое
    1 сезон 10 серия: Поймать рикоразновидности рода Рика
    1 сезон 11 серия: Риксованное дело
    
    Сезон 2
    2 сезон 1 серия: Рик во времени
    2 сезон 2 серия: Успеть до Мортиночи
    2 сезон 3 серия: Аутоэротическая ассимиляция
    2 сезон 4 серия: Вспомрикнуть всё
    2 сезон 5 серия: Пора швифтануться
    2 сезон 6 серия: Рики, наверное, сошли с ума
    2 сезон 7 серия: Большой переполох в маленьком Санчезе
    2 сезон 8 серия: Межпространственный кабель 2: Искушение судьбы
    2 сезон 9 серия: Посмотрите кто сейчас зачищает
    2 сезон 10 серия: Свадебные сквончеры
    
    Сезон 3
    3 сезон 1 серия: Побег из Рикшенка
    3 сезон 2 серия: Рикман с камнем
    3 сезон 3 серия: Огурчик Рик
    3 сезон 4 серия: Заступники 3: Возвращение Губителя Миров
    3 сезон 5 серия: Запутанный грязный заговор
    3 сезон 6 серия: Отдых и Риклаксация
    3 сезон 7 серия: Риклантидическая путаница
    3 сезон 8 серия: Проветренный мозг Морти
    3 сезон 9 серия: Азбука Бет
    3 сезон 10 серия: Рикчжурский Мортидат
    
    Сезон 4
    4 сезон 1 серия: Грань мортущего: Рикви́. Умри. И рикнова
    4 сезон 2 серия: Старик и сиденье
    4 сезон 3 серия: Командуя над гнездом рикушки
    4 сезон 4 серия: Закоготь и подрядок - Специальный Рикпус
    4 сезон 5 серия: Рикный рикейсер Рикактика
    4 сезон 6 серия: БесРиконечный Морти
    4 сезон 7 серия: Промортей
    4 сезон 8 серия: Эпизод с чаном кислоты
    4 сезон 9 серия: Рикя Мортивеческое
    4 сезон 10 серия: Звёздные Морти: Рикращение Джерраев
    
    Сезон 5
    5 сезон 1 серия: Mort Dinner Rick Andre
    5 сезон 2 серия: Мортжественность
    5 сезон 3 серия: Неумортная приквда
    5 сезон 4 серия: Спрень Рикзависимости
    5 сезон 5 серия: Амортиканское Грикффити
    5 сезон 6 серия: Дед Благодарения Рика и Морти
    5 сезон 7 серия: Риквангелион готрового джеррисхождения
    5 сезон 8 серия: Ричное друзьяние чистого мортума
    5 сезон 9 серия: В пРиклёте
    5 сезон 10 серия: Рикмурай Джек
    
    Сезон 6
    6 сезон 1 серия: Солярикс
    6 сезон 2 серия: Рик: Морт спокойно поживал
    6 сезон 3 серия: Двустинкт Бет
    6 сезон 4 серия: Ночная семья
    6 сезон 5 серия: Пункт назначения
    6 сезон 6 серия: Морт Рикского периода
    6 сезон 7 серия: Цельномета оборичка
    6 сезон 8 серия: Анализируй мочу
    6 сезон 9 серия: Первый рикцарь при дворе короля Мортура
    6 сезон 10 серия: Риждественские морникулы
    
    Сезон 7
    7 сезон 1 серия: Как Жопосранчик жопернулся
    7 сезон 2 серия: Ловушка Джеррика
    7 сезон 3 серия: Воздушные силы Вонг
    7 сезон 4 серия: Это Сморть
    7 сезон 5 серия: Незаморченный
    7 сезон 6 серия: Рикщита своей сморти
    7 сезон 7 серия: Влажное Куато-Амортиканское лето
    7 сезон 8 серия: Восставшие цифертиконы в кино
    7 сезон 9 серия: Морт: Рагнарик
    7 сезон 10 серия: Не бойся сморти
    """
