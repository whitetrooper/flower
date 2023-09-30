import turtle

turtle.bgcolor("black")
turtle.speed(500)
turtle.hideturtle()

Colors=["pink","pink","white","white"]

for i in range(120):
    for c in Colors:
        turtle.color(c)
        turtle.circle(200-i,100)
        turtle.lt(90)
        turtle.circle(200-i,100)
        turtle.rt(90)
        turtle.end_fill()

turtle.mainloop()

