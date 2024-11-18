from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for t_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[t_index])
    t.penup()
    t.goto(x=-230, y=y_positions[t_index])
    all_turtles.append(t)


if user_bet:
    is_race_on = True

0
while is_race_on:

    for trt in all_turtles:
        if trt.xcor() > 230:
            is_race_on = False
            winning_color = trt.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rnd_distance = random.randint(0, 10)
        trt.forward(rnd_distance)

screen.exitonclick()
