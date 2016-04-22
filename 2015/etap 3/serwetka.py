from turtle import *
from math import sqrt

def ksztalt(s,kw=True):
    pd()
    l1=[90,90,90,90]
    l2=[45,135,45,135]
    if kw:
        l=l1
    else:
        l=l2
    fillcolor("lightblue")
    begin_fill()
    for i in range(4):
        fd(s)
        lt(l[i])
    end_fill()
    pu()

def composite(s):
    for _ in range(8):
        ksztalt(s,False)
        rt(90)
        ksztalt(s)
        fd(s)
        lt(45)



def serwetka(n):

#    470 = d*n+(n-1)*g = n*(d+g)-g = n*(4*s+ 6*s/sqrt(2))-s-2*s/sqrt(2) = s*(4*n+6*n/sqrt(2)-1-2/sqrt(2))
    fd(470/2)
    bk(470)
    fd(470/2)
    pu()
    s= 470/(4*n+6*n/sqrt(2)-1-2/sqrt(2))
    d = 4*s/sqrt(2)+3*s
    g = s + 2*s/sqrt(2)
    bk(470/2-(s+s/sqrt(2)))
    lt(90)
    bk(s/2)
    lt(90)
    for _ in range(n):
        for _ in range(n):
            composite(s)
            lt(45)
            bk(d)
            rt(45)
        lt(45)
        fd(n*d)

        rt(90)
        bk(d)
        lt(90)
        rt(45)

speed(0)
serwetka(3)
done()