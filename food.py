from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # computer pick a random x and y position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # set the random spot (food) to pop up
        self.goto(random_x, random_y)
        # call the method below. don't write reset() because it's another function
        # inside Turtle class.
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)