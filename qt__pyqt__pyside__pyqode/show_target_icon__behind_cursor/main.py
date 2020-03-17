#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from pathlib2 import Path

from PyQt5.Qt import QApplication, QWidget, QPixmap, QLabel, QTimer, QCursor, Qt


# SOURCE: http://www.pngall.com/target-png/download/12907
FILE_NAME = str(Path(__file__).resolve().parent / 'target.png')


def move_window_to_cursor(widget: QWidget):
    width, height = widget.width(), widget.height()
    pos = QCursor.pos()
    pos.setX(pos.x() - width / 2)
    pos.setY(pos.y() - height / 2)

    widget.move(pos)


if __name__ == '__main__':
    app = QApplication([])

    pix = QPixmap(FILE_NAME)

    mw = QLabel()
    mw.setWindowFlag(Qt.WindowStaysOnTopHint)
    mw.setWindowFlag(Qt.FramelessWindowHint)
    mw.setPixmap(pix)
    mw.setMask(pix.mask())

    mw.show()

    move_window_to_cursor(mw)

    timer = QTimer()
    timer.timeout.connect(lambda: move_window_to_cursor(mw))
    timer.start(33)

    QTimer.singleShot(3000, app.quit)

    app.exec()