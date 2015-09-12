#!/usr/bin/python3

import sys
import shapes
import turtle

def draw_square(area):
    side=shapes.square_side(area)
    turtle.begin_fill()
    turtle.color("red")
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()
    turtle.exitonclick()

def draw_rectangle(area):
    side=shapes.rectangle_side(area)
    turtle.begin_fill()
    turtle.color()
    turtle.forward(side*1.618)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side*1.618)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()
    turtle.exitonclick()
	
def draw_triangle(area):
    side=shapes.triangle_side(area)
    turtle.begin_fill()
    turtle.color()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    turtle.exitonclick()

def draw_circle(area):
    radius=shapes.circle_radius(area)
    turtle.begin_fill()
    turtle.color()	
    turtle.circle(radius)
    turtle.end_fill()
    turtle.exitonclick()

def draw(name,area):
    if name=="CIRCLE":
            draw_circle(area)
    elif name=="SQUARE":
            draw_square(area)
    elif name=="RECTANGLE":
            draw_rectangle(area)
    else:
            draw_triangle(area)

		


if __name__ == "__main__":

	
    area=sys.argv[2]
    name=sys.argv[1]
    draw(name,area)
    
   
