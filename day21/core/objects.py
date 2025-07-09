from turtle import Turtle
from random import randint
from time import sleep


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.reset_ball()

    def bounce_y(self):
        self.setheading((360 - self.heading()) % 360)

    def bounce_x(self):
        self.setheading((180 - self.heading()) % 360)

    def reset_ball(self):
        self.setpos(0,0)
        self.launch()
        sleep(0.5)

    def launch(self):
        random_headings = [randint(30, 150), randint(210, 330)]
        random_dir = random_headings[randint(0,1)] - 90
        self.setheading(random_dir)

    def move(self):
        self.forward(20)

class Player(Turtle):
    def __init__(self,
                 name: str,
                 pos: tuple[float, float],
                 color: str = "blue"):
        super().__init__()
        self._name = name
        self.setpos(pos)
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1.2)
        self.penup()
        self.setpos(pos)

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._name

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

class Scoreboard(Turtle):
    def __init__(self,
                 player: Player,
                 pos: tuple[float, float]):
        super().__init__()
        self.player = player
        self.setpos(pos)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.pencolor("white")
        self.display()


    def add_score(self, val: int):
        self.clear()
        self.score += val
        self.display()

    def display(self):
        self.write(self.score,
                   align="Center",
                   font=("Courier", 50, "bold"))