__author__ = 'apple'


from turtle import *

colors=["blue","orange"]
N=400

def posadzka(n):
    k=400/n
    set_starting_point(n)
    for i in range(n):
        for j in range(n):
            color=colors[(i+j)%2]
            shape(k,color)
            fd(k)
        bk(k*n)
        rt(90)
        fd(k)
        lt(90)

def shape(k,color):
    fillcolor(color)
    l=k/4
    fd(l)
    rt(90)
    fd(l)
    lt(90)
    begin_fill()
    for _ in range(4):
        fd(2*l)
        square(l)
        rt(90)
    end_fill()
    bk(l)
    lt(90)
    fd(l)
    rt(90)



def square(k):
    for _ in range(4):
        fd(k)
        lt(90)

def set_starting_point(n):
    penup()
    bk(N/2)
    lt(90)
    fd(N/2)
    rt(90)


speed(0)
posadzka(3)
done()