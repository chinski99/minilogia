from turtle import *


def shape(n, s):
    for _ in range(2):
        fd(s)
        if n > 1:
            lt(30)
            shape(n - 1, 5 / 8 * s)
            rt(30)
        rt(120)
    fd(s)
    rt(120)


def porost(n):
    lt(90)
    shape(n, 140)


sety(ycor() - 100)
speed(0)
porost(4)
done()
