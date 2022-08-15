# import modules
from turtle import Turtle, Screen
import snake
import time

screen = Screen()
screen.setup(600, 600)
# created the black screen
screen.bgcolor("black")
screen.title("Greedy Serpent")

screen.tracer(0)
gameon = True

snake = snake.Snake()

# key event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# created the snake

# snake.create_snake()
while gameon:
    screen.update()
    snake.start_game()
    time.sleep(0.3)


screen.exitonclick()
