from turtle import Turtle

# In python, constants are named in all Capitals with _
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        # when in main.py call the snake = Snake(), this __init__ auto calls
        # the create_snake method below
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            # to refer to attribute segments, add self
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)