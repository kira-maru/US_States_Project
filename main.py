import turtle
import pandas
from Track import Track
from State_Display import StateDisplay

data = pandas.read_csv("50_states.csv")
STATES = data.state.to_list()
STATES_NUMBER = len(STATES)
GUESSED_STATES = []

tracking = Track()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
display_state = StateDisplay()


def game_on():
    while STATES_NUMBER > 0:
        answer = screen.textinput(title=f"{tracking.score}/{STATES_NUMBER} States correct",
                                  prompt="Type state's name: ").title()
        if answer in STATES:
            display_state.displaying(answer)
            tracking.update_score()
            GUESSED_STATES.append(answer)

        elif answer == "Exit":
            to_learn_states = [state for state in STATES if state not in GUESSED_STATES]
            data_state = pandas.DataFrame(to_learn_states)
            data_state.to_csv("states_to_learn.csv")

            turtle.bye()

        elif answer not in STATES and answer != "Exit":
            continue
        game_on()


game_on()

screen.exitonclick()
