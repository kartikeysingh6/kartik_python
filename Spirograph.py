from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

angle = 0

for i in range(72):
    screen.colormode(255)
    color = random_color()
    turtle.speed("fastest")
    turtle.color(color)
    turtle.circle(100)
    angle += 5
    turtle.setheading(angle)
    
screen.exitonclick()