#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


from _utils import parse, print_stats, URL_DS3


print(URL_DS3)
rows = parse(URL_DS3)
print_stats(rows)
"""
https://darksouls.fandom.com/ru/wiki/Боссы_(Dark_Souls_III)
NAME                                          | HEALTH | SOULS 
----------------------------------------------+--------+-------
Гигант Йорм                                   | 27822  | 36000 
Демон-принц                                   | 21135  | 100000
Отец Ариандель и сестра Фриде                 | 18877  | 72000 
Мидир Пожиратель Тьмы                         | 15895  | 150000
Проклятое Великое древо                       | 15405  | 7000  
Рыцарь-раб Гаэль                              | 14895  | 120000
Лотрик, младший принц и Лориан, старший принц | 13529  | 85000 
Безымянный король                             | 11677  | 80000 
Душа пепла                                    | 10766  | 100000
Оцейрос, Снедаемый король                     | 8087   | 58000 
Древняя виверна                               | 7873   | 70000 
Верховный повелитель Вольнир                  | 7052   | 22000 
Хранитель могилы чемпиона и великий волк      | 6984   | 60000 
Старый король демонов                         | 5301   | 25000 
Танцовщица Холодной долины                    | 5111   | 60000 
Понтифик Саливан                              | 5106   | 28000 
Чемпион Гундир                                | 4956   | 60000 
Олдрик, пожиратель богов                      | 4727   | 50000 
Доспехи драконоборца                          | 4581   | 64000 
Дьяконы глубин                                | 4099   | 13000 
Копье церкви                                  | 3379   | 80000 
Хранители Бездны                              | 3096   | 18000 
Знаток кристальных чар                        | 2723   | 8000  
Вордт из Холодной долины                      | 1328   | 3000  
Судия Гундир                                  | 1037   | 3000  
"""
