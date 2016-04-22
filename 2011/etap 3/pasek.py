from turtle import *
from math import sqrt


def kwadrat(s, col):
    color(col)
    bk(s / 2)
    lt(90)
    bk(s / 2)
    rt(90)
    begin_fill()
    for _ in range(4):
        fd(s)
        lt(90)
    end_fill()
    fd(s / 2)
    lt(90)
    fd(s / 2)
    rt(90)


def edge(x, col):
    l1 = [45, 135, -90, 135, 45, 90]
    color(col)
    begin_fill()
    for a in l1:
        fd(x)
        rt(a)
    end_fill()


def fragment(x):
    s = x * (1 + sqrt(2))
    kwadrat(2 * s, "blue")
    k = s - x / sqrt(2)
    kwadrat(2 * k, "yellow")
    rt(45)
    t = x * (2 + sqrt(2))
    kwadrat(t, "red")
    l = 2 * x
    kwadrat(l, "dark orange")
    lt(45)
    m = x * sqrt(2)
    kwadrat(m, "forest green")
    bk(s)
    lt(90)
    fd(s)
    rt(90)
    for _ in range(4):
        edge(x, "forest green")
        fd(2 * s)
        rt(90)
    lt(90)
    bk(s)
    for _ in range(2):
        rt(45)
        edge(x, "blue")
        lt(45)
        rt(90)
        fd(2 * s)
        rt(90)
    rt(90)
    fd(s)


def pasek(n):
    pu()
    x = 760 / (2 * n * (1 + sqrt(2)))
    s = x * (1 + sqrt(2))
    bk(760 / 2 - s)
    for _ in range(n):
        fragment(x)
        fd(2 * s)


speed(2)
pasek(3)
done()
