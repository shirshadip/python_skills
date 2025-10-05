import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # background color

# Create a turtle
t = turtle.Turtle()
t.color("red")   # pen color
t.pensize(3)     # pen size

# Draw a square
for _ in range(4):
    t.forward(100)  # move forward 100 units
    t.left(90)      # turn left 90 degrees

# Finish
turtle.done()
