from turtle import *
import colorsys

speed(0)
bgcolor("black")
pensize(2)
h = 0

def draw_flower(radius, depth, h):
    if depth == 0:
        return
    col = colorsys.hsv_to_rgb(h, 1, 1)
    color(col)
    circle(radius)
    for i in range(6):
        penup()
        forward(radius)
        pendown()
        draw_flower(radius/2, depth-1, h+0.1)
        penup()
        backward(radius)
        pendown()
        left(60)

draw_flower(100, 3, h)

hideturtle()
done()
