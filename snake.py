import copy
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0),  (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(position)
        self.all_turtles.append(tim)

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def start_game(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # print(self.all_turtles[0].heading())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # print(self.all_turtles[0].heading())

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
