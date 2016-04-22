import turtle as t

B=100


def kwadrat(kolor): #kwadrat
    t.fillcolor(kolor)
    t.begin_fill()
    for i in range(4):
        t.fd(B)
        t.rt(90)
    t.end_fill()

def wsk_romb(kolor): #romb kąty 30,150
    t.fillcolor(kolor)
    t.begin_fill()
    for i in range(2):
        t.fd(100)
        t.rt(30)
        t.fd(100)
        t.rt(150)
    t.end_fill()
        
def szer_romb(kolor): #romb kąty 60,120
    t.fillcolor(kolor)
    t.begin_fill()
    for i in range(2):
        t.fd(100)
        t.rt(60)
        t.fd(100)
        t.rt(120)
    t.end_fill()
        
def owoc():
    t.pu()
    t.lt(30)
    t.fd(B)
    t.lt(30)
    t.fd(B)
    t.seth(300)
    t.pd()


    for i in range(5):         #pierwsza warstwa
        wsk_romb("olive")
        t.rt(30)

    t.lt(30)                        #druga warstwa
    for i in range(4):
        t.fd(B)
        t.lt(30)
        szer_romb("green")
        t.rt(30)
        t.bk(B)
        t.lt(30)

    t.rt(120)                       # trzecia warstwa
    for i in range(3):
        for j in range(2):
            t.fd(B)
            t.lt(30)
        kwadrat("yellow")
        for j in range(2):
            t.rt(30)
            t.bk(B)
        t.lt(30)

    t.rt(30)                        #czwarta warstwa
    for i in range(2):
        for j in range(3):
            t.fd(B)
            t.rt(30)
        t.fd(B)
        t.lt(180)
        szer_romb("orange")
        t.rt(180)
        t.bk(B)
        for j in range(3):
            t.lt(30)
            t.bk(B)
            
        t.lt(30)

    for i in range(5):          #piąta warstwa
        t.fd(B)
        t.rt(30)

    wsk_romb("red")

    


t.speed(0)

owoc()

