# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

color_list = [(250, 246, 243), (248, 245, 246), (212, 154, 98), (242, 249, 247), (236, 241, 245), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211)]


tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()