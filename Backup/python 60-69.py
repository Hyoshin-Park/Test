#60

import turtle

turtle.shape("turtle")

for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()

#61

import turtle

turtle.shape("turtle")

for i in range(0, 3):
    turtle.forward(100)
    turtle.right(120)

turtle.exitonclick()

#62

import turtle

turtle.shape("turtle")

for i in range(0, 360):
    turtle.forward(1)
    turtle.right(1)

turtle.exitonclick()

#63

turtle.shape("turtle")



turtle.color("Black", "Red")
turtle.begin_fill()
for i in range(0, 4):

    turtle.forward(20)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(30)

turtle.pendown()

turtle.color("Green", "blue")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(40)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(50)

turtle.pendown()

turtle.color("blue", "green")
turtle.begin_fill()

for i in range(0, 4):
    turtle.forward(60)
    turtle.right(90)

turtle.end_fill()

turtle.exitonclick()


#64

turtle.shape("turtle")

for i in range(0, 5):
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()

#65

turtle.shape("turtle")

turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)




turtle.exitonclick()

#66

import turtle
import random

turtle.shape("turtle")


for i in range(0, 8):
    color = random.choice(["Black", "red", "green", "yellow", "blue", "purple"])
    turtle.color(color)
    turtle.begin_fill()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(60)
    turtle.left(45)


turtle.exitonclick()

#67

import turtle

for i in range(0, 12):
    turtle.left(30)
    for j in range(0, 8):
        turtle.forward(60)
        turtle.left(45)

turtle.exitonclick()

#68


import turtle
import random

turtle.shape("turtle")


line = random.randint(5, 15)

for i in range(0, line):
    degree = random.randint(0, 360)
    line1 = random.randint(20, 100)
    turtle.forward(line1)
    turtle.right(degree)

turtle.exitonclick()
