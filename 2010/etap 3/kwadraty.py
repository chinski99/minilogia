from turtle import *

def kwadrat(s,col):
    pd()
    fillcolor(col)
    begin_fill()
    for _ in range(4):
        fd(s)
        lt(90)
    end_fill()
    pu()

def trojkat(s,n,col):
    x=position()
    fd(s)
    for i in range(n,0,-2):
        for j in range(i):
            kwadrat(s,col)
            fd(s)
        bk((j+1)*s)
        lt(90)
        fd(s)
        rt(90)
        fd(s)
    setpos(x)

def filling(s,n):
    for _ in range(2):
        trojkat(s,n,"red")
        rt(90)
        bk((n+2)*s)
        trojkat(s,n,"green")
        rt(90)
        bk((n+2)*s)




def kwadraty(n):
    pu()
    k = 2*n+7
    s=480/k
    bk(240)
    lt(90)
    bk(240)
    rt(90)
    color("yellow")
    x=position()
    for i in range(k):
        for j in range(k):
            kwadrat(s,"black")
            fd(s)
        bk(s*k)
        lt(90)
        fd(s)
        rt(90)
    setpos(x)
    fd(s)
    lt(90)
    fd(s)
    rt(90)
    for _ in range(4):
        filling(s,n)
        rt(90)
        bk(2*s*n+5*s)


tracer(30,0)
kwadraty(12)
update()
done()