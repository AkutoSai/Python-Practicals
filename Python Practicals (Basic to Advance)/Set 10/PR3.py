import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(9)
turtle.pencolor("red")
turtle.shape("turtle")
# draw V
turtle.right(65)
turtle.forward(200)
turtle.left(135)
turtle.forward(200)
turtle.penup()
turtle.hideturtle()
turtle.setx(200)
turtle.sety(0)
turtle.pendown()
turtle.showturtle()
# draw Star
for i in range(5):
    turtle.forward(150)
    turtle.right(144)