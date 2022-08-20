# import modules
from turtle import Turtle, Screen
import snake
import time
import food
from  scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
# created the black screen
screen.bgcolor("black")
screen.title("Greedy Serpent")

screen.tracer(0)
gameon = True

snake = snake.Snake()
food = food.Food()
score = ScoreBoard()



# key event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# created the snake
x = 1
# snake.create_snake()
while gameon:
    screen.update()
    snake.start_game()
    time.sleep(x)

    #detect collision

    if snake.head.distance(food) < 15:
        x -= 0.05
        print(x)
        food.change()
        score.add_score()
        snake.extend()

    #collision with wall
    if snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280:
        score.gameover()
        snake.reset()

    #detect collosion with tail
    for segments in snake.all_turtles[1:]:
        if snake.head.distance(segments) < 10:
            score.gameover()
            snake.reset()




screen.exitonclick()
