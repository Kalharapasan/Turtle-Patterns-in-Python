from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
h=0
for i in range(72):
    col=colorsys.hsv_to_rgb(h,1,1)
    color(col)
    forward(200)
    backward(200)
    left(5)
    h+=0.01
hideturtle()
done()
