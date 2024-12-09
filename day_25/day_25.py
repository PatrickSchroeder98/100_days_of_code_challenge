import turtle as trt

import pandas
import pandas as pnd

screen = trt.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
trt.addshape(image)
trt.shape(image)

guessed_states = []

while len(guessed_states) < 50:

    answer_state = str(screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What is another State's name?")).capitalize()
    data = pnd.read_csv('50_states.csv')
    if answer_state == "Exit":
        missing_states = []
        for item in data.state:
            if item not in guessed_states:
                missing_states.append(item)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for item in data.state:
        if answer_state == item:
            t = trt.Turtle()
            t.hideturtle()
            t.penup()
            coordinates = data[data.state == answer_state]
            t.goto(int(coordinates.x.item()), int(coordinates.y.item()))
            t.write(coordinates.state.item())
            guessed_states.append(answer_state)

