import turtle
import pandas
from Track import Track
from State_Display import StateDisplay

data = pandas.read_csv("50_states.csv")
STATES = data.state.to_list()
STATES_NUMBER = len(STATES)
GUESSED_STATES = []
TO_LEARN_STATES = []

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
            for missing_state in STATES:
                if missing_state not in GUESSED_STATES:
                    TO_LEARN_STATES.append(missing_state)
            data_state = pandas.DataFrame(TO_LEARN_STATES)
            data_state.to_csv("states_to_learn.csv")

            turtle.bye()

        elif answer not in STATES and answer != "Exit":
            continue
        game_on()


game_on()

screen.exitonclick()
