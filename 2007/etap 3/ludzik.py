__author__ = 'apple'

from turtle import *

outl = [(1, 90), (3, -90), (2, 90), (1, 90), (1, -90), (1, -90), (1, 90), (1, 90), (1, 90), (1, -90), (1, -90), (1, 90),
        (1, 90), (2, -90), (3, 90), (1, 90), (2, -90), (1, 90), (1, -90), (2, 90)]
dirs = [(0, 1), (0, 1), (-1, 0), (0, 1), (-1, 0), (-1, 0), (3, 0), (1, 0), (1, 0), (-2, 1), (0, 1), (2, 0), (-1, -1),
        (0, 0)]


def ludzik(n):
    outline()
    for l, r in dirs:
        lines_in_square(n)
        move(l, r)


def outline():
    a = 100 / 1.41
    penup()
    bk(150)
    rt(90)
    fd(200)
    pendown()
    rt(90 + 45)
    for n, angle in outl:
        fd(a * n)
        rt(angle)


def line_up(l):
    x = heading()
    setheading(90)
    pendown()
    fd(l)
    bk(l)
    penup()
    setheading(x)


def lines_in_square(n):
    a = 100 / 1.41
    k = (n - 1) // 2
    s = a / (k + 1)
    line_up(100)
    for i in range(k):
        fd(s)
        t = a - (s * (i + 1))
        line_up(t / 1.41 * 2)
    bk(s * k)
    rt(90)
    for i in range(k):
        fd(s)
        t = a - (s * (i + 1))
        line_up(t / 1.41 * 2)
    bk(s * k)
    lt(90)


def move(l, r):
    penup()
    a = 100 / 1.41
    fd(l * a)
    rt(90)
    fd(r * a)
    lt(90)
    pendown()


speed(0)
ludzik(5)
done()
