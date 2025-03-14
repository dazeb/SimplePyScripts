#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


from _utils import parse, print_stats, URL_DS1, URL_DS2, URL_DS3

rows = []
for game, url in {
    "DS1": URL_DS1,
    "DS2": URL_DS2,
    "DS3": URL_DS3,
}.items():
    for name, health, souls in parse(url):
        rows.append((game, name, health, souls))

print_stats(
    rows,
    headers=("GAME", "NAME", "HEALTH", "SOULS"),
    sort_column=3,
)
"""
GAME | NAME                                          | HEALTH | SOULS 
-----+-----------------------------------------------+--------+-------
DS3  | Мидир Пожиратель Тьмы                         | 15895  | 150000
DS2  | Древний Дракон                                | 19840  | 120000
DS3  | Рыцарь-раб Гаэль                              | 14895  | 120000
DS3  | Душа пепла                                    | 10766  | 100000
DS3  | Демон-принц                                   | 21135  | 100000
DS2  | Син Дремлющий дракон                          | 10030  | 96000 
DS2  | Сгоревший Король Слоновой Кости               | 8040   | 92000 
DS2  | Нашандра                                      | 8770   | 90000 
DS2  | Вендрик                                       | 11450  | 90000 
DS3  | Лотрик, младший принц и Лориан, старший принц | 13529  | 85000 
DS2  | Дымный рыцарь                                 | 10100  | 84000 
DS2  | Сэр Алонн                                     | 10140  | 80000 
DS3  | Безымянный король                             | 11677  | 80000 
DS3  | Копье церкви                                  | 3379   | 80000 
DS2  | Аава, питомец короля                          | 8930   | 78000 
DS2  | Повелитель гигантов                           | 5970   | 75000 
DS2  | Старый Демон из Плавильни                     | 9260   | 75000 
DS2  | Скверная королева Элана                       | 9280   | 72000 
DS3  | Отец Ариандель и сестра Фриде                 | 18877  | 72000 
DS1  | Гвин Повелитель Пепла                         | 4250   | 70000 
DS3  | Древняя виверна                               | 7873   | 70000 
DS2  | Защитник трона и Смотритель трона             | 6670   | 68000 
DS3  | Доспехи драконоборца                          | 4581   | 64000 
DS1  | Ложе Хаоса                                    | 14     | 60000 
DS1  | Нагой Сит                                     | 6355   | 60000 
DS1  | Четыре Короля                                 | 9504   | 60000 
DS1  | Нито Повелитель Могил                         | 4300   | 60000 
DS1  | Манус Отец Бездны                             | 6666   | 60000 
DS1  | Черный дракон Каламит                         | 5940   | 60000 
DS2  | Варг, Церах и Разорительница Гробниц          | 9200   | 60000 
DS3  | Танцовщица Холодной долины                    | 5111   | 60000 
DS3  | Чемпион Гундир                                | 4956   | 60000 
DS3  | Хранитель могилы чемпиона и великий волк      | 6984   | 60000 
DS3  | Оцейрос, Снедаемый король                     | 8087   | 58000 
DS2  | Луд и Заллен                                  | 10140  | 56000 
DS1  | Орнштейн и Смоуг                              | 4286   | 50000 
DS1  | Арториас Путник Бездны                        | 3750   | 50000 
DS2  | Вельстадт Королевский защитник                | 6290   | 50000 
DS3  | Олдрик, пожиратель богов                      | 4727   | 50000 
DS2  | Старый Железный Король                        | 6070   | 48000 
DS2  | Гниющий                                       | 7080   | 47000 
DS2  | Забытая Грешница                              | 3560   | 45000 
DS2  | Фрея, Возлюбленная Герцога                    | 4220   | 42000 
DS1  | Сиф Великий Волк                              | 3432   | 40000 
DS1  | Железный голем                                | 2923   | 40000 
DS1  | Демон-стоног                                  | 3432   | 40000 
DS1  | Гвиндолин Темное Солнце                       | 2000   | 40000 
DS2  | Дракон-Страж                                  | 5270   | 37000 
DS3  | Гигант Йорм                                   | 27822  | 36000 
DS2  | Прячущийся во тьме                            | 5770   | 35000 
DS2  | Зеркальный рыцарь                             | 6540   | 34000 
DS2  | Стражи Руин                                   | 6990   | 33000 
DS2  | Демон из Плавильни                            | 5970   | 32000 
DS1  | Присцилла Полукровка                          | 2458   | 30000 
DS1  | Страж Святилища                               | 3060   | 30000 
DS3  | Понтифик Саливан                              | 5106   | 28000 
DS2  | Два Драконьих всадника                        | 3822   | 26000 
DS2  | Демон песни                                   | 6180   | 26000 
DS1  | Разверстый Дракон                             | 4401   | 25000 
DS2  | Горгульи с башни                              | 14005  | 25000 
DS3  | Старый король демонов                         | 5301   | 25000 
DS2  | Скорпион Нажка                                | 5741   | 23000 
DS3  | Верховный повелитель Вольнир                  | 7052   | 22000 
DS1  | Квилег Ведьма Хаоса                           | 3139   | 20000 
DS1  | Бродячий Демон                                | 5250   | 20000 
DS1  | Неутомимый воин                               | 4200   | 20000 
DS1  | Мудрый демон Огня                             | 5448   | 20000 
DS2  | Мита Губительная королева                     | 3570   | 20000 
DS2  | Колесница палача                              | 4140   | 19000 
DS3  | Хранители Бездны                              | 3096   | 18000 
DS2  | Преследователь                                | 3110   | 17000 
DS1  | Вихрь                                         | 1326   | 15000 
DS2  | Повелители скелетов                           | 2080   | 15000 
DS2  | Древний Драконоборец                          | 2880   | 15000 
DS2  | Гибкий часовой                                | 3150   | 14000 
DS2  | Командир крысиной гвардии                     | 4310   | 14000 
DS2  | Алчный Демон                                  | 4440   | 13000 
DS3  | Дьяконы глубин                                | 4099   | 13000 
DS2  | Драконий всадник                              | 3050   | 12000 
DS2  | Боец крысиной гвардии                         | 1410   | 11000 
DS1  | Горгулья                                      | 1479   | 10000 
DS1  | Лунная Бабочка                                | 1506   | 10000 
DS2  | Последний Гигант                              | 2530   | 10000 
DS3  | Знаток кристальных чар                        | 2723   | 8000  
DS2  | Странствующий маг и прихожане                 | 2300   | 7000  
DS3  | Проклятое Великое древо                       | 15405  | 7000  
DS1  | Демон Капра                                   | 1176   | 6000  
DS1  | Демон-Телец                                   | 1250   | 3000  
DS3  | Судия Гундир                                  | 1037   | 3000  
DS3  | Вордт из Холодной долины                      | 1328   | 3000  
DS1  | Демон Прибежища                               | 813    | 2000  
DS2  | Алдия, ученый Первородного Греха              | 6800   | 0     
"""
