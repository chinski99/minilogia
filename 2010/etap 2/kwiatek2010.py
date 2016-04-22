from turtle import *


def romb(k, a, c, cir=False):
    fillcolor(c)
    begin_fill()
    for _ in range(2):
        fd(k)
        lt(a)
        fd(k)
        lt(180 - a)
    end_fill()
    if cir:
        fd(k)
        lt(a)
        fd(k)
        rt(90 + a / 2)
        fillcolor("yellow")
        begin_fill()
        circle(12.5)
        end_fill()
        lt(90 + a / 2)
        bk(k)
        rt(a)
        bk(k)


def kwiatek(n):
    a = 180 / (2 * n + 1)
    for i in range(n):
        romb(200, a, "orange")
        lt(a)
        romb(100, a, "green", True)
        lt(a)
    romb(200, a, "orange")


speed(0)
kwiatek(2)
done()
