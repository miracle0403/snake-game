from turtle import Turtle, Screen
screen = Screen()
screen.setup(600, 600)
all_turtles = []
x = 0
for turtle in range(1, 4):
    tim = "tim" + str(turtle)
    tim = Turtle()
    tim.color("white")
    tim.shape("square")
    if turtle > 1:
        x -= 20
        tim.setx(x)
    all_turtles.append(tim)

print(all_turtles)

#created the black screen
screen.bgcolor("black")
screen.title("Greedy Serpent")

#created the snake






screen.listen()
screen.exitonclick()