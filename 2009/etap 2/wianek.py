__author__ = 'apple'

from turtle import *

fig1 = ([30, 150, 30, 150], "green")
fig2 = ([60, 120, 60, 120], "orange")
fig3 = ([90, 90, 90, 90], "blue")

k = 80


def figure(desc):
    ang, col = desc
    fillcolor(col)
    begin_fill()
    for i in ang:
        fd(k)
        lt(i)
    end_fill()


def composite():
    figure(fig1)
    lt(30)
    figure(fig2)
    fd(k)
    rt(30)
    figure(fig3)
    lt(30)
    bk(k)
    rt(30)


def wianek():
    for _ in range(6):
        composite()
        fd(k)
        rt(360 / 6)


wianek()
done()
