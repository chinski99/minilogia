from turtle import *


def pent(s):
    pd()
    for _ in range(5):
        fd(s)
        lt(360 / 5)
    pu()


def compo(s):
    for _ in range(5):
        pent(s)
        fd(s)
        rt(360 / 5)


def wing(s):
    pd()
    for _ in range(3):
        fd(s);
        rt(72)
    lt(2 * 72);
    fd(s)
    rt(36);
    fd(s)
    lt(72);
    fd(s)
    rt(72);
    fd(s)
    rt(72)
    compo(s)
    pd()
    x = pos()
    a = heading()
    lt(72 + 72);
    fd(s)
    rt(36);
    fd(s)
    lt(72);
    fd(s)
    rt(72);
    fd(s)
    rt(72)
    compo(s)
    setpos(x)
    setheading(a)
    fd(s)
    rt(72)
    lt(72 + 72);
    fd(s)
    rt(36);
    fd(s)
    lt(72);
    fd(s)
    rt(72);
    fd(s)
    rt(72)
    compo(s)


def kwiatek():
    s = 25
    rt(180)
    compo(s)
    for _ in range(5):
        x = pos()
        a = heading()
        wing(s)
        setpos(x)
        setheading(a)
        fd(s)
        rt(72)


speed(0)
kwiatek()
done()
