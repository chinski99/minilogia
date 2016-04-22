import turtle as t

side=50

def hexagon(level,color):
    t.pu()
    t.home()
    t.lt(30)
    t.fd(level*side)
    t.pd()
    t.rt(120)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(6):
        t.fd(level*side)
        t.rt(60)
    t.end_fill()

def star():
    t.fillcolor("green")
    for i in range(6):
        t.begin_fill()
        for k in range(2):
            t.fd(side)
            t.rt(60)
            t.fd(side)
            t.rt(120)
        t.end_fill()
        t.rt(60)
            
    


hexagon(6,"red")
hexagon(3,"green")
hexagon(2,"red")
t.pu()
t.home()
t.lt(30)
t.pd()
star()
for i in range(6):
    t.pu()
    t.fd(4*side)
    t.pd()
    star()
    t.pu()
    t.bk(4*side)
    t.rt(60)




