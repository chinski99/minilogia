from turtle import *

def bukiet(n,dif):
    lt(90)
    for _ in range(n):
        x=position()
        y=heading()
        kwiat(dif)
        setposition(x)
        setheading(y)
        rt(360/n)



def kwiat(dif):
    pendown()
    fd(200)
    d=80
    while (d>=10):
        rt(60)
        fd(d)
        d-=dif
    penup()

bukiet(3,5)
done()

