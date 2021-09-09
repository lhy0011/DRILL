import turtle

count = 6
x = -100
y = -150

while (count > 0):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    y += 100
    count -= 1

count = 6
y = -150
turtle.left(90)

while (count > 0):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    x += 100
    count -= 1

