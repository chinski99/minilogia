__author__ = 'apple'

from turtle import *

N=400

def rect(a,b,col): # od środka
    fillcolor(col)
    bk(a/2)
    lt(90)
    fd(b/2)
    rt(90)
    begin_fill()
    for _ in range(2):
        fd(a)
        rt(90)
        fd(b)
        rt(90)
    end_fill()
    fd(a/2)
    rt(90)
    fd(b/2)
    lt(90)

def dywan(n):
    penup()
    k=2*(2*n+2)+1    #ilość kratek w zależności od n
    b=N/k            #bok kratki
    rect(N,N,"lightgreen")
    l=(n+1)*b        #odległość od środka do środka pomarańczowego kwadratu

    for _ in range(4):
        fd(l)
        lt(90)
        fd(l)
        rt(90)
        p=(2*n+1)*b   #bok pomarańczowego kwadratu
        rect(p,p,"orange")
        bk(l)
        rt(90)
        fd(l)

    for _ in range(4):   # poprzeczki w czterech kierunkach
        for i in range(n):
            fd(2*b)
            rect(b,(2*(i+1)+1)*b,"lightgreen")
        bk(2*n*b)
        rt(90)

#speed(0)
dywan(6)
done()
