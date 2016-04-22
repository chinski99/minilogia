from turtle import *
from math import sqrt


def shape(s):
    sety(ycor() - 2 * s)
    lt(45)
    pd()
    fillcolor('green')
    begin_fill()
    for _ in range(4):
        trace(s)
    end_fill()
    pu()
    rt(45)
    sety(ycor() + 2 * s)


def trace(s):
    b = s * sqrt(2)
    t = [(2 * b, 90), (b, 45), (s, -90), (s, -90), (s, 45), (b, 90)]
    for x, k in t:
        fd(x)
        rt(k)


def wycinanka(n):
    k = 7 * n + 3 * (n - 1)
    s = 480 / k
    penup()
    setpos(pos() - (240, -3.5 * s))

    for _ in range(n):
        p = pos()
        for _ in range(n):
            shape(s)
            setpos(pos() + (5 * s, 5 * s))
        setpos(p + (5 * s, -5 * s))


speed(0)
wycinanka(5)
done()
