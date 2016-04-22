from turtle import *

def posadzka(n):
    l=450/(8*n+8)
    bk(225)
    lt(90)
    bk(225)
    rt(90)
    fillcolor("yellow")
    begin_fill()
    for _ in range(4):
        fd(450)
        lt(90)
    end_fill()
    for _ in range(4):
        fd(8*l)
        siatka(n,"dark green",klocek,90)
        fd(450-8*l)
        lt(90)
    lt(90)
    for _ in range(4):
        fd(8*l)
        siatka(n,"light green",klocek2,-90)
        fd(450-8*l)
        rt(90)

def klocek(l,col):
    pd()
    fillcolor(col)
    begin_fill()
    for _ in range(2):
        fd(2*l);lt(90)
        for _ in range(2):
            fd(l);rt(90)
            fd(l);lt(90)
        fd(2*l);lt(90)
    end_fill()
    pu()

def klocek2(l,col):
    pd()
    fillcolor(col)
    begin_fill()
    for _ in range(2):
        fd(2*l);rt(90)
        for _ in range(2):
            fd(l);lt(90)
            fd(l);rt(90)
        fd(2*l);rt(90)
    end_fill()
    pu()

def siatka(n,col,el,angle):
    l=450/(8*n+8)
    for i in range(n):
        for j in range(n-i):
            el(l,col)
            fd(4*l);lt(angle)
            fd(4*l);rt(angle)
        bk((j+1)*4*l);lt(angle)
        bk((j+1)*4*l);rt(angle)
        fd(8*l)
    bk(n*8*l)

speed(0)
posadzka(4)
done()