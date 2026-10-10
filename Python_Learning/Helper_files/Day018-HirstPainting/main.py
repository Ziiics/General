from idlelib.util import fix_x11_paste

import colorgram
import turtle as t
import random

# get rgb colors palette from the jpg

colors= colorgram.extract('color_palette.jpg',10)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)


# doing the dots

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)

def turning(level):
    if level % 2 == 1:
        tim.left(90)
    else:
        tim.right(90)

def draw(level):
    for x in range(level):
        for y in range(level):
            tim.color(random.choice(rgb_colors))
            tim.pd()
            tim.dot(20)
            tim.pu()
            tim.forward(50)
        turning(x)
        tim.forward(50)
        turning(x)
        tim.forward(50)

draw(15)