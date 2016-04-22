__author__ = 'apple'

from turtle import *


def szary(n):
    pendown()
    fillcolor("grey")
    begin_fill()
    k=2*n+1
    s=760/k
    bk(760/2)
    fd(760)
    lt(90)
    fd(4*s)
    lt(90)
    fd(s)
    lt(90)
    fd(s)
    rt(90)
    fd(s)
    rt(90)
    fd(s)
    lt(90)
    fd(s)
    lt(90)
    fd(s)
    rt(90)
    fd(760-4*s)
    rt(90)
    fd(s)
    lt(90)
    fd(s)
    lt(90)
    fd(4*s)
    lt(90)
    end_fill()
    penup()

def zamek(n):
    penup()
    k=2*n+1
    s=760/k

    szary(n)
    x=position()
    lt(90)
    fd(4*s)
    rt(90)
    triangle(s)

    fd(2*(n-1)*s)
    triangle(s)
    fd(2*s)
    triangle(s)
    setposition(x)
    fd(s)
    lt(90)
    fd(s)
    rt(90)
    for _ in range(n):
        okno(s)
        fd(2*s)

def triangle(s):
    pendown()
    z=1.25*s
    y=0.25*s/2
    x=heading()
    setheading(0)
    bk(y)
    fillcolor('red')
    begin_fill()
    for _ in range(3):
        fd(z)
        lt(120)
    end_fill()
    fd(y)
    setheading(x)
    penup()

def okno(s):
    pendown()
    fillcolor('blue')
    begin_fill()
    for _ in range(4):
        fd(s)
        lt(90)
    end_fill()
    lt(45)
    fd(s*1.41)
    lt(135)
    fd(s)
    lt(135)
    fd(s*1.41)
    lt(45)
    bk(s)
    penup()

zamek(9)
done()