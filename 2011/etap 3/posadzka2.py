from turtle import *
from math import sqrt


def octo(k):
    s = k / sqrt(2)
    fd(s)
    fillcolor("grey")
    pd()
    begin_fill()
    for _ in range(8):
        fd(k)
        lt(45)
    end_fill()
    pu()
    bk(s)


def posadzka():
    pu()
    setpos(pos() - (230, 230))
    fillcolor("darkgreen")
    begin_fill()
    for _ in range(4):
        fd(460)
        lt(90)
    end_fill()
    setpos(pos() - (10, 10))
    n = 30
    l = 480 / n
    for _ in range(4):
        k = l / (1 + sqrt(2))
        for _ in range(4):
            for _ in range(n):
                octo(k)
                fd(l)
            lt(90)
        setpos(pos() + (l, l))
        n = (n - 2) // 2  # 30 14 6 2
        l = l * 2


speed(0)
posadzka()
done()
