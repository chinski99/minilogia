__author__ = 'apple'

from turtle import *
from random import randint

def kwiatek():
    N=56
    base(N)


def base(N):
    centered_hexagon(N, "darkgreen")
    centered_hexagon(N / 3, "yellow")
    lt(90)
    fd(N/3)
    for _ in range(6):
        hex("lightgreen",N/3)
        rt(120)
        fd(N/3)
        lt(60)
    fd(2*N/3)
    rt(120)
    pendown()
    for _ in range(6):
        color("black")
        galaz(N)
        color("red")
        fd(N)
        rt(60)


def galaz(N):
    r=randint(1,9)
    x=position()
    for i in range(r):
        s=N-i*7
        trojkat(s)
        lt(60)
        fd(s)
        rt(60)
        penup()
        bk((N-(i+1)*7)/2)
        pendown()
    penup()
    setposition(x)
    pendown()

def trojkat(s):
    fillcolor("darkgreen")
    begin_fill()
    for _ in range(3):
        fd(s)
        lt(120)
    end_fill()



def centered_hexagon(n, col):
    penup()
    lt(90)
    fd(n)
    rt(120)
    hex(col, n)
    lt(120)
    bk(n)
    rt(90)


def hex(col, n):
    pendown()
    fillcolor(col)
    begin_fill()
    for _ in range(6):
        fd(n)
        rt(360 / 6)
    end_fill()
    penup()




speed(0)
kwiatek()
done()