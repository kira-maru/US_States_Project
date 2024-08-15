from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")
STATES = data.state.to_list()
X_COR = data.x
Y_COR = data.y


class StateDisplay(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def displaying(self, answer):
        answer_index = STATES.index(answer)
        self.goto(X_COR[answer_index], Y_COR[answer_index])
        self.write(f"{answer}")

