import turtle
import random
import math
turtle.speed(0)
turtle.color("blue")
turtle.up()
turtle.goto(250,3)

phi=(1+math.sqrt(5))/2
i=360/2*phi*math.pi
t=turtle
t.down()

for x in range(233):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("red")

for x in range(144):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("green")
    
for x in range(55):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("yellow")

for x in range(89):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("blue")

for x in range(89):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("blue")

for x in range(200):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("yellow")

for x in range(80):
    t.right(i)
    u=i
    t.forward(600)

    turtle.color("blue")

for x in range(89):
    t.right(i)
    u=i
    t.forward(600)
