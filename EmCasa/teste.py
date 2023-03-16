import turtle

# create a turtle object
heart = turtle.Turtle()

# set the fill color of the heart
heart.fillcolor('red')

# start filling the heart
heart.begin_fill()

# draw the heart shape using a series of arcs
heart.left(140)
heart.forward(180)
heart.circle(-90, 200)
heart.setheading(60)
heart.circle(-90, 200)
heart.forward(180)

# end filling the heart
heart.end_fill()

# move the turtle to the center of the heart
heart.penup()
heart.goto(0, 100)
heart.pendown()

# write text inside the heart
heart.color('white')
heart.write("Momô eu te amo!", align="center", font=("Arial", 18, "bold"))

# hide the turtle cursor
heart.hideturtle()

# wait for the user to close the window
turtle.done()

