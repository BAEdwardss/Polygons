#Initialize

import turtle
import random
t=turtle.Turtle()
t.speed(99999)


#Functions

def drawTriangle(size,color):
    t.color(color)
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.rt(120)
    t.end_fill()

def drawPolygon(n, size, color):
    if n >= 3:
        t.penup()
        xran=random.randint(-200,100)
        yran=random.randint(-200,100)
        t.goto(xran, yran)
        t.pendown()
        t.color(color)
        t.begin_fill()
        for i in range(n):
            t.fd(size)
            t.rt(360/n)
        t.end_fill()
    elif n <=3:
        print("input error: a polygon has at least three sides!")


#Main
drawPolygon(6, 150, "red")
drawPolygon(5, 200, "blue")
drawPolygon(3, 50, "orange")
drawPolygon(2, 300, "purple")
drawPolygon(1, 400, "black")
drawPolygon(10, 30, "yellow")
drawPolygon(4, 200, "black")
