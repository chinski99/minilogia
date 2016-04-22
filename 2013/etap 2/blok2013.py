from turtle import *




def kubik2(s,n):
    k=s/4
    bp=pos()
    sety(ycor()-s)
    square(s,"orange")
    for _ in range(n):
        p=pos()
        for _ in range(2):
            for _ in range(4):
                lt(90)
                pd()
                fd(s)
                pu()
                bk(s)
                rt(90)
                fd(k)
            lt(90)
        setpos(p+(k,k))
        seth(0)
        s=s/2
        k=s/4
    square(4*k,"blue")
    setpos(bp)



def square(s, col):
    pendown()
    fillcolor(col)
    begin_fill()
    for _ in range(4):
        fd(s)
        lt(90)
    end_fill()
    penup()


def blok():
    k = 448 / 16  # wys 16 szer 22
    pu()
    setpos(pos() - (11 * k, -8 * k))
    bp = pos()
    for _ in range(4):
        p = pos()
        for _ in range(5):
            kubik2(4 * k, 3)
            sety(ycor() - 3 * k)
        setpos(p)
        setx(xcor() + 6 * k)
    setpos(bp)
    setpos(pos() + (3 * k, -3 * k))
    for _ in range(3):
        p = pos()
        for _ in range(3):
            kubik2(4 * k, 1)
            sety(ycor() - 3 * k)
        setpos(p + (6 * k, 0))


speed(0)
blok()
done()
