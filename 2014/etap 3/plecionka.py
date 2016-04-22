

from turtle import  *

def simple(a,col):
    pendown()
    fillcolor(col)
    begin_fill()
    lt(30)
    fd(3*a)
    lt(120)
    fd(a)
    lt(60)
    fd(2*a)
    rt(60)
    fd(2*a)
    lt(60)
    fd(a)
    lt(120)
    fd(3*a)
    end_fill()
    lt(30)
    penup()

def compo(a):
    c=["brown","orange","yellow"]
    for i in range(3):
        simple(a,c[i])
        rt(120)

def pile(a,n):
    for _ in range(n):
        compo(a)
        lt(90)
        bk(4*a)
        rt(90)

def plecionka(n):
    penup()
    bk(200)
    lt(90)
    fd(200)
    rt(90)
    a=480/(4*n+1)
    for i in reversed(range(n)):
        pile(a,i+1)
        lt(90)
        fd(4*a*(i+1))
        rt(120)
        fd(4*a)
        lt(30)


plecionka(6)
done()
