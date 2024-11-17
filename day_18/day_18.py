# import colorgram as cl

# rgb_colors = []
# colors = cl.extract('image.jpg', 30)

# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	new_color = (r, g, b)
# 	rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as trt
import random

color_list = [
    (23, 16, 95),
    (154, 13, 30),
    (233, 42, 5),
    (40, 182, 158),
    (126, 253, 207),
    (238, 70, 167),
    (209, 179, 209),
    (246, 218, 19),
    (39, 133, 243),
    (246, 219, 4),
    (208, 148, 179),
    (126, 156, 205),
    (224, 67, 45),
    (105, 189, 174),
    (223, 135, 119),
    (81, 86, 136),
    (153, 62, 75),
    (44, 37, 105),
    (242, 168, 156),
    (176, 184, 222),
    (110, 9, 24),
    (184, 26, 11),
    (148, 207, 220),
]

t = trt.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
trt.colormode(255)

t.setheading(225)
t.forward(300)
t.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)

        t.forward(500)
        t.setheading(0)

screen = trt.Screen()
screen.exitonclick()
