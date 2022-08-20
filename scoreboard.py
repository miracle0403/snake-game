from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.writer()
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score += 1
        self.writer()

    def gameover(self):
        self.goto(0, 0)
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.clear()
        self.write(f"GAME OVER \n Score: {self.score} High Score: {self.highscore}", True, align="center")
        self.clear()
        self.writer()

    def writer(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", True, align="center")

