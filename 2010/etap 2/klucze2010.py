from turtle import *

def shape(k):
    pendown()
    l = [(1,90),(7,-90),(2,-90),(2,-90),(2,90),(1,90),(3,90),(4,90),(4,90),(8,90)]
    begin_fill()
    for s,a in l:
        fd(s*k)
        rt(a)
    end_fill()
    penup()

def klucze():
    pencolor("orange")
    fillcolor("green")
    k=420/(12*1.41)
    pensize(2)
    for _ in range(2):
        for _ in range(3):
            shape(k)
            rt(90)
            fd(k*4)
        rt(90)
        fd(k*4)
        rt(180)


penup()
speed(0)
lt(135)
klucze()

done()