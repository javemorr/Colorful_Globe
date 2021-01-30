# Hour of Code HK - Python Workshop #4
# Date: 17 Jan 2021

# Use Random, Turtle
import random
from random import randint
import turtle as t


# Function -> Get Line Length()
# Parameter list -> Empty
# Get user input to define the line length

def get_line_length(): # alternative getLineLength()
    choice = input('Enter line length "long, medium, short":')
    print (choice)
    
    if choice == 'long':
        line = 250

    elif choice == 'medium':
        line = 200

    else:
        line = 50
        

    return line

# Function -> Get Line Width()
# Parameter list -> Empty
# User input :  (superthick, thick, thin) -> 40, 25, 10

def get_line_width():
    choice = input('Enter line width "superthick, thick, thin":')
    print (choice)
    
    if choice == 'superthick':
        line = 40

    elif choice == 'thick':
        line = 25

    else:
        line = 5
        
    return line
    
# Function *TODO* => Inside Window()
# Give a bounding box for the movement of the turtle (at the end of this program)
def inside_window():
    (x, y) = t.pos()
    inside = 10000 < x*x + y*y < 90000
    return inside
    
# Function *TODO* => Move Turtle()
# Control the randomized movement of the turtle

def move_turtle(line_length):

    #t.shapesize(1,1,1)
    #t.stamp()
    t.forward(line_length)

# main program
line_length = get_line_length()
line_width = get_line_width()
print('The return value is', line_length)
print('The return value is', line_width)

t.shape('turtle')
t.pensize(line_width)
t.bgcolor('black')
t.goto(200,0)

i = 0


# An Infinite Loop for the turtle movement
while True:
    pen_color = ['red', 'orangered', 'orange', 'yellow', 'greenyellow', 'green', 'turquoise', 'blue', 'blueviolet', 'indigo', 'purple', 'violetred']

    if inside_window():
        t.pencolor(pen_color[i])
        t.fillcolor(pen_color[i])
      
        value = randint(3,20)
        polygon_angle = 360/value

        rotation = randint(1,2)
        if rotation == 1:
            t.right(polygon_angle)
        else:
            t.left(polygon_angle)

        move_turtle(line_length)
        i = (i + 1)%11

# Give a bounding box for the movement of the turtle

    else:   
        t.pencolor('black')
        t.fillcolor('black')
        t.right(180)
        move_turtle(line_length)
        i = i - 1

        

    



