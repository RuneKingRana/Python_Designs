from turtle import *
import colorsys as cs
bgcolor('black')
pensize(2)
tracer (2)
h=0

for i in range(329):
    c=cs.hsv_to_rgb(h,1,1)
    h+=0.008
    pencolor (c)
    pensize(3)
    circle(i, 100)
    rt(91)
    fillcolor('black')
    begin_fill()
    circle(i/2,90)
    end_fill()
    rt(91)
    circle(60,90)
done()