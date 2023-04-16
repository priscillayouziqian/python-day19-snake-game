from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # compare this turtle with another turtle, the result is their distance
    # in this case, detect collision (crash) with food.
    # why 15? not 0? we have to consider the width/height of the spot
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    # too far on the right? or too far on the left?
    # too far on the top? or bottom?
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()