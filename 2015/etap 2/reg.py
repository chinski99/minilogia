__author__ = 'apple'

from turtle import *
from random import randint

K = 20


def reg(szer, n):  # szerokość regału, liczba półek
    start_position(szer, n)
    regal(szer, n)
    fd(K)
    for _ in range(n):
        polka(szer // K - 2)
        up(7)


def polka(k):
    rect(k * K, 6*K, "white")
    pendown()
    for _ in range(k):
        r = randint(1, 3)
        if r == 1:
            rect(K, 3 * K, "red")
        elif r == 2:
            rect(K, 4 * K, "green")
        elif r == 3:
            rect(K, 5 * K, "darkblue")
        fd(K)
    penup()
    bk(k * K)


def rect(a, b, col):
    fillcolor(col)
    begin_fill()
    for _ in range(2):
        fd(a)
        lt(90)
        fd(b)
        lt(90)
    end_fill()


def border(szer):
    rect(K, K, "sienna")
    fd(szer - K)
    rect(K, K, "sienna")
    bk(szer - K)


def up(k):
    lt(90)
    fd(k * K)
    rt(90)


def start_position(szer, n):
    penup()
    bk(szer / 2)
    up(-(n * 7 + 3) / 2)


def regal(szer, n):
    border(szer)
    up(1)
    rect(szer, n * 7 * K + K, "sienna")
    up(n * 7 + 1)
    border(szer)
    up(-n * 7)


#speed(0)
reg(300, 4)
done()
