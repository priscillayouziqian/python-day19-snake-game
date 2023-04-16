from turtle import Turtle
# set these constants for future easy change setting style purposes.
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        # hide the default arrow
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # don't write .clear(), so we can still see the scores on top although we lose the game

    def increase_score(self):
        self.score += 1
        # before new score increase, clear the board, otherwise, score
        # will overlap in the same space
        self.clear()
        self.update_scoreboard()