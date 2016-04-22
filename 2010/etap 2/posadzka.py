from turtle import *
from math import sqrt

def basic(a):
    b=a*sqrt(2)
    fillcolor("lightyellow")
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(135)
    fd(b)
    rt(135)
    end_fill()
    fillcolor("lightgreen")
    begin_fill()
    fd(a)
    rt(90)
    fd(a)
    rt(135)
    fd(b)
    lt(135)
    end_fill()

def posadzka(n):
    pu()
    bk(225)
    lt(90)
    bk(225)
    rt(90)
    pd()
    for _ in range(4):
        basic(225)
        fd(450)
        lt(90)
    k=225*sqrt(2)
    l=k/n
    fd(225)
    lt(45)
    for _ in range(n):
        for _ in range(n):
            basic(l)
            fd(l)
        bk(n*l)
        lt(90)
        fd(l)
        rt(90)

posadzka(3)
done()
