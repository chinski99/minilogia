from turtle import *


def rol(n):
    for _ in range(2):
        fd(n)
        rt(60)
        fd(n)
        rt(120)


def rop(n):
    for _ in range(2):
        fd(n)
        lt(60)
        fd(n)
        lt(120)


def shape(n):
    fillcolor("green")
    begin_fill()
    rop(n)
    end_fill()
    fd(n)
    lt(60)
    fd(n)
    rt(60)
    begin_fill()
    rol(n)
    end_fill()
    fd(n)
    rt(60)
    fd(n)
    lt(60)


def posadzka():
    penup()
    a = 510 / 34
    lt(120)
    fd(a)
    rt(120)
    bk(16 * a)
    for _ in range(6):
        for i in range(11, 5, -1):
            for _ in range(i):
                shape(a)
            bk(3 * a * i)
            lt(60)
            fd(3 * a)
            rt(60)
        bk(a)
        rt(60)
        fd(2 * a)


speed(0)
posadzka()
done()
