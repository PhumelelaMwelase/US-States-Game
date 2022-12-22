import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# answer_state = screen.textinput(title="States Correct", prompt="What's another state's name?:")

data = pandas.read_csv("50_states.csv")

list_of_states = []
for state in data.state:
    list_of_states.append(state)

correct_guesses = 0
guessed_states = []

while correct_guesses < 50:
    if correct_guesses == 0:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                        prompt="What's the name of a state?:").title()
    elif correct_guesses == 1:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 State Correct",
                                        prompt="What's another state's name?:").title()
    else:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct",
                                        prompt="What's another state's name?:").title()

    if answer_state == "Exit":
        # Generate list of states not guessed by the user
        unguessed = [state for state in list_of_states if state not in guessed_states]

        new_data = pandas.DataFrame(unguessed)
        new_data.to_csv("new_file.csv")

        break

    for state in list_of_states:
        if state == answer_state:
            correct_answer = (data[data.state == answer_state])
            x_coor = int(correct_answer.x)
            y_coor = int(correct_answer.y)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x_coor, y_coor)
            t.write(answer_state)
            correct_guesses += 1
            guessed_states.append(answer_state)


#
turtle.mainloop()

# screen.exitonclick()
