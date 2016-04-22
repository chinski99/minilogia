from turtle import *


def square(s, col):
    pendown()
    fillcolor(col)
    begin_fill()
    for _ in range(4):
        fd(s)
        lt(90)
    end_fill()
    penup()


def line(s, col, n):
    for _ in range(n):
        square(s, col)
        fd(s)


def shape1(s, col):  # 11 10 9 6 5 2
    x = position()
    y = heading()
    lt(90)
    l = [11, 9, 8, 5, 4, 1]
    for i in l:
        line(s, col, i)
        bk(s)
        rt(90)
    setposition(x)
    setheading(y)


def shape2(s, col):  # 11 10 9 6 5 2
    x = position()
    y = heading()
    lt(90)
    l = [11, 10, 9, 6, 5, 2]
    for i in l:
        line(s, col, i)
        lt(90)
    setposition(x)
    setheading(y)


def fullshape(s, col):
    shape1(s, col)
    shape2(s, col)


def move(x, y, s):
    fd(x * s)
    lt(90)
    fd(y * s)
    rt(90)


def dlugi(s, n):
    shape1(s, "green")
    for _ in range(n - 1):
        move(22, 0, s)
        fullshape(s, "green")
    move(22, 0, s)
    shape2(s, "green")
    move(-12, 11, s)
    rt(180)
    for _ in range(n):
        fullshape(s, "orange")
        move(22, 0, s)
    rt(180)
    move(11 + 4 + 19 * n + 3 * (n - 1), -12, s)


def krotki(s):
    dlugi(s, 1)


def motyw(n):
    l = 600
    k = l / (26 + 19 * n + 3 * (n - 1))
    penup()
    bk(300)
    move(11, 11, k)
    dlugi(k, n)
    rt(90)
    krotki(k)
    rt(90)
    dlugi(k, n)
    rt(90)
    krotki(k)




tracer(10,0)
motyw(4)
update()

done()
