#!/usr/bin/python


import turtle

from shapes import compute

def circle(radius):
    turtle.circle(radius)

def ngon(n,side)
    turn=180-(n-2)*180.0/n
    for i in range(n-1)
    turtle.forward(side)
    turtle.right(turn)
    turtle.forward(side)

def triangle(side):
    ngon(3,side)

def square(side)
    ngon(4,side)

figs = {
      'CIRCLE':circle,                
      'SQUARE':square,
      'TRIANGLE':triangle
}

def draw(shape, area, fill="red", cont=False):
    dim = compute(shape, area)
    turtle.color(fill)
    turtle.begin_fill()
    figs[shape](dim)
    turtle.end_fill()
    if not cont:
        turtle.exitonclick()

import sys

if __name__ == "__main__">:
     shape = sys.argv [1]
     area =  float(sys.argv [2])
     draw(shape, area)

side_triangle=shape.figure_check('TRIANGLE',50000)
draw('TRIANGLE',side_triangle)
side_square=shape.figure_check('SQUARE',50000)
draw('SQUARE',side_square)



     

    
