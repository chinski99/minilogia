from turtle import *
from math import sin


def wianek(s):
    for _ in range(5):
        romb(s,"violet")
        rt(360/10)
        romb(s,"yellow")
        rt(360/10)

def romb(s,col):
    pd()
    fillcolor(col)
    begin_fill()
    lt(18)
    for _ in range(2):
        fd(s)
        rt(36)
        fd(s)
        rt(180-36)
    end_fill()
    rt(18)
    pu()

def wianki():
    l=25
    pu()
    lt(18)
    bk(l)
    rt(36)
    bk(l)
    lt(18)
    for _ in range(2):
        for i in range(10):
            wianek(l)
            lt(90)
            fd(l)
            lt(36)
            fd(2*l)
            rt(36)
            fd(l)
            rt(90)
            lt(36)
        lt(18)
        fd(l)
        rt(36)
        fd(2*l)
        lt(36)
        fd(l)
        rt(18)
        rt(180)

tracer(30,0)
wianki()
home()
pd()
fd(350)
bk(700)
fd(350)
lt(90)
fd(100)
bk(200)
update()
done()