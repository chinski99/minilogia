__author__ = 'apple'

from turtle import *

r=10
l=40

def gwiazdka(n):
    k=360/n
    rt(k/2)
    color("blue")
    for _ in range(n):
        lt(k/2+90)
        pu()
        fd(10)
        pd()
        fd(l-10)
        kulka(r,"blue")
        rt(k)
        fd(l)
        kulka(r,"blue")
        lt(k/2)
        fd(l)
        kulka(r,"blue")
        rt(90)
        fd(l)
        kulka(r,"blue")
        rt(90)
        fd(l)
        kulka(r,"blue")
        lt(k/2)
        fd(l)
        kulka(r,"blue")
        rt(k)
        fd(l-10)
        pu()
        fd(10)
        pd()
        kulka(r,"orange")
        rt(k/2+270)



def kulka(r,col):
    color(col)
    x=heading()
    setheading(0)
    fd(r)
    lt(90)
    fillcolor(col)
    begin_fill()
    circle(r)
    end_fill()
    rt(90)
    bk(r)
    color("blue")
    setheading(x)

speed(0)
gwiazdka(7)
done()