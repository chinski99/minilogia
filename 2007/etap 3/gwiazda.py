from turtle import *
from math import *


def tri(l, c):
    fillcolor(c)
    begin_fill()
    fd(l * sqrt(2))
    lt(135)
    fd(l)
    lt(90)
    fd(l)
    lt(135)
    end_fill()


def c1(l):
    tri(l, "blue")
    lt(45)
    fd(l * 2)
    lt(135)
    tri(l, "blue")
    lt(45)
    fd(l / 2)
    lt(45)
    tri(l / 2, "yellow")
    rt(45)
    fd(l)
    rt(135)
    tri(l / 2, "yellow")
    lt(135)
    fd(l / 2)
    lt(135)
    fd(l * sqrt(2))


def cz(l):
    x = pos()
    c1(l)
    c1(l)
    lt(135)
    fd(l * 2)
    rt(135)
    fd(l / 2 * sqrt(2))
    lt(90)
    c1(l)
    pu()
    setpos(x)
    pd()
    rt(90)


def gwiazda(p):
    l = p / 2 / sqrt(2)
    pu()
    lt(90)
    fd(p)
    rt(90 + (350 / 6 / 2))
    pd()
    for i in range(6):
        cz(l)
        fd(p)
        rt(360 / 6)


tracer(30, 0)
gwiazda(100)
update()
done()
