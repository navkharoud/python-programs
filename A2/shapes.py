"""
Gurparteek Singh
PHYS-2112

"""
import math
import turtle

#Draws a pie, then moves into position to the right.
def draw_pie(t, n, r):
    draw_polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

#Draws a pie divided into radial segments.
def draw_polypie(t, n, r):
    #calculate angle
    angle = 360.0 / n
    for _ in range(n):
        draw_isosceles(t, r, angle/2)
        t.lt(angle)

#Draws an icosceles triangle.
def draw_isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    #onto the next angle direction
    t.lt(180-angle)

bob = turtle.Turtle()
size = 50
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
turtle.mainloop()