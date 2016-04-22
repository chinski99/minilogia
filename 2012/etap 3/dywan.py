from turtle import *


def element(level, k):
    fillcolor("red")
    begin_fill()
    for _ in range(4):
        fd(k)
        lt(90)
    end_fill()
    if level>1:
        for _ in range(3):
            fd(k)
            rt(90)
            element(level - 1, k/2)
            lt(180)
        fd(k)
        lt(90)


def dywan(n):
    penup()
    bk(80)
    rt(90)
    fd(80)
    lt(90)
    element(0, 160)
    for _ in range(4):
        fd(160)
        rt(90)
        element(n, 80)
        lt(180)


speed(0)
dywan(3)
done()
