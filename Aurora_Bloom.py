from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
h=0
for i in range(60):
    col=colorsys.hsv_to_rgb(h,1,1)
    color(col)
    circle(100)
    left(360/12)
    h+=0.02
hideturtle()
done()
