from turtle import *

speed(0)

def day():
    color("yellow")
    pensize(2)
    begin_fill()
    for i in range(18):
        forward(70)
        left(100)
    end_fill()

def back():
    color("skyblue")
    begin_fill()
    goto(-250,-150)
    for i in range(4):
        forward(500)
        left(90)
    end_fill()
    color("forestgreen")
    begin_fill()
    for i in range(4):
        forward(500)
        right(90)
    end_fill()

def dom():
    color("dimgray")
    begin_fill()
    for i in range(4):
        forward(150)
        left(90)
    end_fill()
    color("steelblue")
    penup()
    forward(10)
    left(90)
    forward(90)
    right(90)
    for i in range(2): 
        begin_fill()
        for i in range(4):
            forward(50)
            left(90)
        end_fill()
        forward(80)
    left(180)
    forward(30)
    left(90)
    forward(30)
    right(90)
    for i in range(2): 
        begin_fill()
        for i in range(4):
            forward(50)
            left(90)
        end_fill()
        forward(80)

def kyst():
    color("darkgreen")
    right(90)
    begin_fill()
    circle(50,180)
    end_fill()
