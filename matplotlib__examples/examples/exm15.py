__author__ = "ipetrash"


# Использование библиотеки Matplotlib. Как отобразить легенду
# Легендой называют табличку, в которой показано какой график какой линией нарисован.
# Чтобы показать легенду, нужно вызвать функцию legend() из пакета pylab. Есть
# несколько способов для добавления легенды.

import math

# Импортируем один из пакетов Matplotlib
import pylab

# Импортируем пакет со вспомогательными функциями
from matplotlib__examples import mlab


# Будем рисовать график этой функции
def func(x):
    """
    sinc (x)
    """
    if x == 0:
        return 1.0
    return math.sin(x) / x


if __name__ == "__main__":
    # Интервал изменения переменной по оси X
    xmin = -20.0
    xmax = 20.0

    # Шаг между точками
    dx = 0.01

    # Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
    xlist = mlab.frange(xmin, xmax, dx)

    # Вычислим значение функции в заданных точках
    ylist1 = [func(x) for x in xlist]
    ylist2 = [func(x * 0.2) for x in xlist]

    ## Первый способ
    # В качестве параметра функции legend() нужно передать список или кортеж,
    # содержащий столько элементов, сколько графиков нарисовано в рабочем окне.
    # Элементов может быть и меньше, но в этом случае последние графики, на которых
    # не хватит элементов кортежа или списка, останутся без подписей.
    # Следующий пример рисует два графика и к каждому из них добавляет описание в
    # виде легенды.

    # Нарисуем два одномерных графика
    pylab.plot(xlist, ylist1, "b-")
    pylab.plot(xlist, ylist2, "g--")

    # !!! Добавим легенду.
    # !!! Первому графику будет соответствовать надпись "f(x)",
    # !!! А второму - "f(0.2 * x)"
    pylab.legend(("f(x)", "f(0.2 * x)"))
    ## Первый способ

    ## Второй способ
    # Того же самого результата мы можем добиться, если при рисовании графиков
    # будем использовать дополнительный параметр label, а затем вызовем функцию
    # legend() без параметров.
    # !!! Нарисуем два одномерных графика и сразу зададим их описание
    # pylab.plot (xlist, ylist1, "b-", label = "f(x)")
    # pylab.plot (xlist, ylist2, "g--", label = "f(0.2 * x)")
    #
    # # !!! Добавим легенду.
    # pylab.legend ()
    # Этот способ более удобен тем, что каждому графику сразу приписывается какая-то
    # метка.
    ## Второй способ

    ## Заголовок легенды
    # В легенду можно добавить заголовок, для этого в функцию legend() надо
    # передать дополнительный строковый параметр title со строкой заголовка.
    # !!! Добавим легенду с заголовком
    # pylab.legend (title = "Sinc")
    ## Заголовок легенды

    # Покажем окно с нарисованным графиком
    pylab.show()
