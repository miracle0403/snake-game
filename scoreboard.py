from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align="center")
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align="center")

    def gameover(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER \n Score: {self.score}", True, align="center")