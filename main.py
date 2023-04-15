from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()

# use key binding (event listeners)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # use .update() to refresh the screen
    screen.update()
    # use the timer to delay the refresh to control how often it happens
    time.sleep(0.1)

    snake.move()



screen.exitonclick()