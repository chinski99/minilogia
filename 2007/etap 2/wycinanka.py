from turtle import *
from math import sqrt


def wycinanka(n):
    s = 700 / (2 * n)
    pu()
    setpos(pos() + (-350, s / 2))
    for _ in range(2):
        for _ in range(n):
            ksztalt(s)
            fd(2 * s)
        rt(90)
        fd(s)
        rt(90)


def kwadrat(s):
    lt(45)
    for _ in range(4):
        fd(s)
        rt(90)
    rt(45)


def ksztalt(s):
    pd()
    z = s / sqrt(2)
    kwadrat(z)
    fd(s)
    kwadrat(z)
    fd(s)
    lt(120)
    fd(s)
    lt(60)
    kwadrat(z)
    fd(s)
    lt(60)
    fd(s)
    lt(120)
    pu()


speed(0)
wycinanka(6)
done()
