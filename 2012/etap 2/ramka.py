__author__ = 'apple'

# ilość kratek 11 + 5 + n * 8

from turtle import *


def shape(a):
    pendown()
    fillcolor("orange")
    begin_fill()
    b = 1.41 * a
    for _ in range(2):
        fd(a)
        lt(45)
        fd(b)
        rt(90)
        fd(b)
        lt(45)
        fd(a)
        lt(90)
        fd(a)
        lt(45)
        fd(b)
        rt(90)
        fd(b)
        rt(90)
        fd(3 * b)
        lt(90)
        fd(4 * b)
        lt(45)
        fd(a)
        lt(90)

    end_fill()
    penup()


def square():
    penup()
    bk(240)
    lt(90)
    fd(240)
    rt(90)
    pendown()
    fillcolor('green')
    begin_fill()
    for _ in range(4):
        fd(480)
        rt(90)
    end_fill()


def warstwa(n, bok):
    k = 11 + 5 + (n - 1) * 8
    s = bok / k
    rt(90)
    fd(5 * s)
    lt(90)
    for _ in range(4):
        for _ in range(n):
            shape(s)
            fd(8 * s)
        fd(3 * s)
        lt(90)
        fd(5 * s)
        rt(180)


def wypelnienie(n):
    bok = 480
    k = 11 + 5 + (n - 1) * 8
    s = bok / k
    for _ in range(n):
        warstwa(n, bok)
        fd(5 * s)
        bok = bok - 10 * s
        s = bok / k


speed(0)
square()
wypelnienie(5)
done()
