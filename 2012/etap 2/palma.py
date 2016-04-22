__author__ = 'apple'

from turtle import *

def trojkat(size,col):
    pendown()
    fillcolor(col)
    begin_fill()
    for _ in range(3):
        fd(size)
        lt(120)
    end_fill()
    penup()

def romb(size,col):
    pendown()
    fillcolor(col)
    begin_fill()
    lt(60)
    for _ in range(2):
        fd(size)
        lt(60)
        fd(size)
        lt(120)
    end_fill()
    rt(60)
    penup()

def piatka(size):
    romb(size,"brown")
    fd(size)
    romb(size,"brown")
    bk(size)
    lt(120)
    fd(size)
    rt(120)
    for _ in range(3):
        romb(size,"brown")
        fd(size)
    bk(3*size)
    lt(60)
    fd(size)
    rt(60)


def pien(wys,size):
    for _ in range(3):
        trojkat(size,"brown")
        fd(size)
    bk(2*size)
    for _ in range(wys):
        piatka(size)

def galaz(liscie,size,kat):
    for _ in range(liscie):
        romb(size,"green")
        lt(60)
        fd(size)
        lt(60)
        fd(size)
        rt(120)
        lt(kat)

def korona(size):
    x=position()
    galaz(7,size,30)
    setposition(x)
    setheading(0)
    fd(size)
    x=position()
    galaz(7,size,-30)
    setposition(x)
    setheading(0)
    lt(120)
    fd(size)
    rt(120)
    romb(size,"green")
    lt(60)
    fd(size)
    lt(60)
    fd(size)
    rt(120)
    x=position()
    galaz(6,size,30)
    setposition(x)
    setheading(0)
    galaz(6,size,-30)


speed(0)
pien(7,15)
korona(15)

done()