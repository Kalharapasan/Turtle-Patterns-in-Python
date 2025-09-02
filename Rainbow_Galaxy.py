from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
pensize(2)

n = 36
h = 0

for i in range(360):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.005
    circle(i, 60)
    left(10)

hideturtle()
done()
