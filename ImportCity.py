from City import *
speed(0)
back()

def move(x, y):
    penup()
    goto(x, y)
    pendown()

move(-150, 120)
day()

move(0,-10)
dom()
seth(0)

move(0,-160)
dom()

move(0,-170)
kyst()

right(90)
move(-50,-170)
kyst()

exitonclick()
hideturtle()
