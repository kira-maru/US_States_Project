from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")
STATES = data.state.to_list()
STATES_NUMBER = len(STATES)


class Track(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.clear()
        self.score += 1



