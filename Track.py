from turtle import Turtle

class Track(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.clear()
        self.score += 1



