import turtle

def draw_square(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)

def draw_cross_of_squares(length):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

 
    draw_square(length)


    turtle.penup()
    turtle.goto(0, length)
    turtle.pendown()
    draw_square(length)

 
    turtle.penup()
    turtle.goto(length, 0)
    turtle.pendown()
    draw_square(length)


    turtle.penup()
    turtle.goto(0, -length)
    turtle.pendown()
    draw_square(length)

  
    turtle.penup()
    turtle.goto(-length, 0)
    turtle.pendown()
    draw_square(length)

turtle.speed(3)
draw_cross_of_squares(50)
turtle.hideturtle()
turtle.done()