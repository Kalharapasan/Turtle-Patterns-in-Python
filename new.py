from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
h = 0

for i in range(75):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.014
    left(1)
    forward(1)
    for j in range(2):
        left(2)
        circle(140)

hideturtle()
done()


#####################################

from turtle import *
from colorsys import *

setposition(0, -60)
tracer(20)
bgcolor("black")
h = 0
pensize(2)

for i in range(230):
    pencolor(hsv_to_rgb(h, 1, 1))
    begin_fill()
    circle(-20, 240)
    right(59)
    forward(i * 0.5)
    circle(40, 120)
    left(120)
    backward(i * 0.5)
    h += 0.005
    end_fill()

done()

#########################################

from turtle import *
import colorsys

speed(0)
bgcolor("black")
pensize(2)
R = 0

for i in range(122):
    color(colorsys.hsv_to_rgb(R, 1, 1))
    R += 0.010
    rt(70)
    fd(i)
    circle(i, -10)
    lt(100)
    up()
    fd(i)
    down()
    circle(i * 2, -90)

hideturtle()
done()

#########################################################
from turtle import *
from colorsys import *

tracer(500)
bgcolor("black")
h = 0
pensize(2)

for i in range(270):
    h += 0.0015
    color(hsv_to_rgb(h, 1, 1))
    up()
    fd(i / 2)
    goto(0, 0)
    down()
    rt(60)
    fillcolor("black")
    begin_fill()
    circle(-i, 60)
    end_fill()
    rt(144)
    for j in range(3):
        circle(i * 2, 90)
    rt(108)

hideturtle()
done()

#########################################################
from turtle import *

bgcolor("black")
color("orange")
speed(0)

for i in range(400):
    fd(i)
    rt(98)

hideturtle()
done()
#########################################################
from turtle import *

setposition(-60, 0)
speed(0)
bgcolor('black')
colors = ['orange', 'white']
pensize(2)

for i in range(150):
    color(colors[i % 2])
    rt(i)
    circle(90, i)
    up()
    fd(i + 50)
    down()
    rt(90)
    fd(i - 65)

hideturtle()
done()
#########################################################
from turtle import *
from random import *

speed(0)
bgcolor('black')
colors = ["orange", "gold", "white"]

for i in range(20):
    for j in range(9):
        for k in range(2):
            color(choice(colors))
            circle(40 + i * 5, 90)
            fd(100)
            lt(90)
    rt(45)

hideturtle()
done()
#########################################################
from turtle import *
from colorsys import *

bgcolor("black")
tracer(20)
hideturtle()
c = 0
n = 1
p = True
up()
goto(-150, -60)
down()

while True:
    c += 0.0004
    color(hsv_to_rgb(c, 1, 1))
    circle(n)

    if p:
        n = n - 1
    else:
        n = n + 1
        left(3)
        fd(2)

    if n == 0 or n == 60:
        p = not p
        rt(4)
        fd(1.5)

done()
#########################################################
import turtle as t
import random

t.speed(1000)
t.bgcolor("black")
t.pensize(1)
colors = ["white", "gold"]

for i in range(100):
    t.lt(145)
    for j in range(5):
        n = random.choice(colors)
        t.color(n)
        t.fd(250)
        t.lt(150)
    t.hideturtle()

t.done()
#########################################################
import turtle as t
import colorsys

s = t.Screen()
t.title("StudyMuch")
t.bgcolor('black')
t.tracer(10)
m = 0.9
n = 95

for i in range(450):
    c = colorsys.hsv_to_rgb(m, 1, 1)
    m += 0.005
    t.pencolor(c)
    t.right(90)
    t.forward(i + 1)
    t.left(90)
    t.forward(i)
    t.circle(2, n)
    t.left(120)
    t.circle(m, 1)
    
t.hideturtle()
t.done()
#########################################################
from turtle import *

tracer(10)
bgcolor("black")
colors = ['white', 'orange']

for i in range(205):
    color(colors[i % 2])
    rt(i)
    circle(200, i + 2)
    fd(i)
    right(180)
    fd(i)

hideturtle()
done()
#########################################################
from turtle import *
from colorsys import *

speed(0)
bgcolor('black')
h = 1

for i in range(140):
    h -= 0.0015
    color(hsv_to_rgb(h, 1, 1))
    right(70)
    forward(i * 2)
    circle(i * 2, -10)
    left(100)
    up()
    forward(i)
    down()
    circle(i * 2, -90)
    right(230)

done()
#########################################################
fd(f)
circle(c, 210)
rt(138)
circle(c, 210)
fd(f)
end_fill()

penup()
goto(-50, -70)
pendown()
heart(140, 70)

penup()
goto(70, 70)
pendown()
left(40)
heart(100, 50)

style = ("arial", 50, "bold",)
penup()
goto(-175, -150)
pendown()
write("I Love You", font=style, move=True)

hideturtle()
done()
#########################################################

from turtle import *

speed(0)
bgcolor("black")
c = ["red", "yellow", "green", "purple", "orange", "blue"]

hideturtle()

for i in range(140):
    pencolor(c[i % 6])
    width(i / 30)
    forward(i)
    left(120)
    
    for j in range(2):
        forward(i)
        right(90)

done()

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################


#########################################################

#########################################################

#########################################################

#########################################################

#########################################################

#########################################################