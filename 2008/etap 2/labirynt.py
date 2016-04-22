from turtle import *


def elem(n,dir):
    pd()
    t=10
    for i in range(n):
        bk(dir*2*t+dir*i*2*t)
        lt(90)
        fd(2*t+i*2*t)
        rt(90)
        if (i == n-1):
            bk(dir*10)
            fd(dir*10)
        fd(dir*t+dir*i*2*t)
        rt(90)
        fd(t)
        lt(90)
        fd(dir*2*t)
        rt(90)
        fd(2*t+i*2*t)
        lt(90)
    pu()

def labirynt(n):
    for k in range(2):
        x=pos()
        elem(n,1)
        setpos(x)
        setheading(k*180)
        bk(30+2*n*10)
        x=pos()
        elem(n,-1)
        setpos(x)
        sety(ycor()-(2*n-1)*10)
        rt(180)


speed(0)
labirynt(5)
done()