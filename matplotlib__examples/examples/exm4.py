__author__ = "ipetrash"


# Для рисования кругового графика используется функция pie() из модуля pylab.
# В простейшем случае в эту функцию достаточно передать всего лишь данные,
# которые определяют площадь соответствующего сектора.


import pylab

if __name__ == "__main__":
    # Данные для построения графика
    data = [20.0, 10.0, 5.0, 1.0, 0.5]

    # Нарисовать круговой график
    pylab.pie(data)

    pylab.show()
