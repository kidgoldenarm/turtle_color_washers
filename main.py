from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()
screen.colormode(255)
screen.screensize(700, 700)
screen.bgcolor("black")

tim.hideturtle()


def rand_color():
    for rando in range(0, 3):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
    return rgb


def row_dots():
    tim.speed("fastest")
    tim.dot(90, rand_color())
    tim.forward(10)
    tim.dot(85, "black")
    tim.dot(83, rand_color())
    tim.back(2)
    tim.dot(74, "black")


def next_row():
    tim.penup()
    tim.setpos(random.randint(-260, 261), random.randint(-260, 261))


for dots in range(160):
    next_row()
    row_dots()


screen.exitonclick()