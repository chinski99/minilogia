from turtle import *

a = 7


def shape():
    pendown()
    fillcolor("blue")
    begin_fill()
    lt(45)
    for i in range(2):
        fd(a)
        rt(45)
        fd(a)
        rt(45)
        fd(a)
        rt(90)
    end_fill()
    rt(45)
    penup()


def square():
    pendown()
    fillcolor("orange")
    begin_fill()
    lt(45)
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()
    rt(45)
    penup()


def complete():
    square()
    lt(45)
    fd(a)
    rt(45)
    shape()
    rt(45)
    fd(a)
    lt(90)
    bk(a)
    rt(45)
    shape()
    rt(45)
    fd(a)
    lt(45)
    fd(a)
    for _ in range(3):
        square()
        lt(45)
        fd(a)
        rt(90)
        bk(a)
        lt(45)
    rt(45)
    fd(2 * a)
    lt(90)
    bk(2 * a)
    rt(45)


def complete2():
    x = position()
    complete()
    complete()
    setposition(x)


def muszka(n):
    for _ in range(2):
        for i in range(1, n + 1):
            x = position()
            for j in range(i):
                complete2()
                rt(45)
                fd(2 * a)
                lt(90)
                bk(2 * a)
                rt(45)
            setposition(x)
            lt(45)
            fd(2 * a)
            rt(45)
            fd(a)
            lt(45)
            fd(a)
            rt(90)
            fd(a)
            lt(45)
            fd(a)
        home()
        rt(180)


speed(0)
muszka(5)
done()
