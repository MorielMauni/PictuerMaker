#import colorgram

# Get 10 colors out of 'hirst_spot_painting.jpg'
#colors = colorgram.extract('hirst_spot_painting.jpg', 15)

# Empty List for the colors
#rgb_colors = []

# For loop to add all the RGB colors to the list
#for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colors.append(new_color)

# To check the list and copy it
#print(rgb_colors)

#------------------------------------------------
# Color List that was created with colorgram and the white colors were deleted
color_list = [(198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
              (16, 22, 55), (66, 9, 49),]

# Imports
import turtle
from turtle import *
import random

# Name the Turtle moudle
tim = Turtle()
# Hide the Turtule image
tim.hideturtle()
# To use RGB colors
turtle.colormode(255)

def screen():
    """Make the screen stay until you click"""
    screen = Screen()
    screen.exitonclick()
def move_pen():
    """Make the pen go up and move 50 steps"""
    tim.penup()
    tim.forward(50)

def tim_strat():
    """Get the 'Turtle' to the strat point to create a new line """
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
#------------------------------------------------
# Gets the 'Turtle' to the Begining point and make sure the speed
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

num_dots = 100
# For Loop for the dots, size of dot is 20, space between dots is 50, The picture is 10x10.
for dot_count in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    move_pen()
    if dot_count % 10 ==0:
        tim_strat()

screen()

