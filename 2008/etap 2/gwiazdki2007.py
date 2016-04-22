from turtle import *
from math import sqrt

def gwiazdki():
    l=50
    shape(l)
    for _ in range(5):
        x=pos()
        y=heading()
        fd(l)
        lt(18)
        fd(l)
        lt(18)
        shape(l)
        setpos(x)
        setheading(y)
        rt(72)

def triangle(a):
    fd(a)
    lt(135)
    fd(a*sqrt(2))
    lt(135)
    fd(a)
    lt(90)

def shape(l): # 18 54
    lt(45+180-9)
    pendown()
    fillcolor("green")
    begin_fill()
    for _ in range(5):
        triangle(l)
        rt(72)
    end_fill()
    penup()

lt(45+180)
speed(0)
gwiazdki()



done()