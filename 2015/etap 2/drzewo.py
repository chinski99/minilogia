

from turtle import *

l=20 #bok trójkąta
k=30 #długość łodygi

def drzewo(n):
    punkt_startu(n)
    color("green")
    a=60
    for i in reversed(range(n)):
        fd(2*k)
        lodyga(a,i+1)
        a=-a
    fd(2*k)
    lodyga(a)
    fd(2*k)
    lodyga(-a)
    fd(2*k)

def trojkat():
    fillcolor("green")
    begin_fill()
    rt(30)
    for _ in range(3):
        fd(l)
        lt(120)
    end_fill()
    lt(30)

def listek(a):
    lt(a)
    fd(k)
    trojkat()
    bk(k)
    rt(a)

def lodyga(a,n=0):
    lt(a)
    for _ in range(n):
        fd(k)
        listek(60)
        listek(-60)
    fd(k)
    bk(k*(n+1))
    rt(a)


def punkt_startu(n):
    penup()
    lt(90)
    bk((n+3)*k)
    pendown()

speed(0)
drzewo(5)
