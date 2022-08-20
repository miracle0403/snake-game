from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_high_score()
        self.penup()
        self.color("white")
        self.writer()
        self.hideturtle()


    def write_high_score(self):
        with open("highscore.txt", mode="w") as highs:
            highs.write(f"{self.highscore}")

    def read_high_score(self):
        with open("highscore.txt") as highers:
            file = highers.read()
            files = int(file)
            return files

    def add_score(self):
        self.clear()
        self.score += 1
        self.writer()

    def gameover(self):
        self.goto(0, 0)
        highscore = self.read_high_score()
        print(highscore)
        if self.score > highscore:
            self.highscore = self.score
            self.write_high_score()
        self.score = 0
        self.clear()
        self.write(f"GAME OVER \n Score: {self.score} High Score: {self.highscore}", True, align="center")
        self.clear()
        self.writer()

    def writer(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", True, align="center")

