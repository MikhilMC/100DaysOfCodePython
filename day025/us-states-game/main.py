import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinates)
#
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()

correct_guesses = []

while True:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state name?"
    ).title()

    if answer_state == "Exit":
        break

    state_data = data[data.state == answer_state]
    if len(state_data) != 0 and answer_state not in correct_guesses:
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        state_name.goto(x_cor, y_cor)
        state_name.write(answer_state)
        correct_guesses.append(answer_state)
        screen.title(titlestring=f"{len(correct_guesses)}/50 states")

# states_to_learn.csv
data_dict = {"state": [], "x": [], "y": []}
for state_name in state_list:
    if state_name not in correct_guesses:
        data_dict["state"].append(state_name)
        state_data = data[data.state == state_name]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        data_dict["x"].append(x_cor)
        data_dict["y"].append(y_cor)

remaining_states = pandas.DataFrame(data_dict)
remaining_states.to_csv("states_to_learn.csv")


screen.exitonclick()
