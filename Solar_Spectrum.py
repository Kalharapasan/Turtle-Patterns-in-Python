from turtle import *
import colorsys
speed(0)
bgcolor("black")
pensize(2)
h=0
for i in range(36):
    col=colorsys.hsv_to_rgb(h,1,1)
    color(col)
    begin_fill()
    circle(100,60)
    left(120)
    circle(100,60)
    end_fill()
    left(10)
    h+=0.05
hideturtle()
done()
