from turtle import Turtle
from random import randint

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
SCOREBOARD_POSITION = (0, 240)
SCOREBOARD_FONT = ("Courier", 24, "bold")
SCOREBOARD_ALIGNMENT = "center"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeSegment(Turtle):
    def __init__(self, x: float | tuple[float, float], y: float | None = None):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        if isinstance(x, tuple) and not y:
            self.goto(x)
        else:
            self.goto(x, y)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(SCOREBOARD_POSITION)
        self.display()

    def display(self):
        self.write(f"Score: {self.score}",
                   align=SCOREBOARD_ALIGNMENT,
                   font=SCOREBOARD_FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER",
                   align=SCOREBOARD_ALIGNMENT,
                   font=SCOREBOARD_FONT)

    def update(self, value):
        self.clear()
        self.score += value
        self.display()

class Snake:
    def __init__(self):
        self.segments = [SnakeSegment(cord) for cord in STARTING_POSITIONS]

    def __getitem__(self, index):
        return self.segments[index]

    def __len__(self):
        return len(self.segments)

    def __add__(self, new_segment: SnakeSegment):
        return self.segments.append(new_segment)

    @property
    def body(self):
        return self.segments

    @property
    def head(self):
        return self.segments[0]

    @property
    def tail(self):
        return self.segments[-1]

    @property
    def direction(self):
        return self.head.heading()

    def move(self):
        positions = [seg.pos() for seg in self.segments]
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(positions[i - 1])
        self.head.forward(MOVE_DISTANCE)

    def direct(self, new_heading: int):
        if not abs(180 - self.head.heading()) == new_heading:
            self.head.setheading(new_heading)

    def up(self):
        self.direct(UP)

    def down(self):
        self.direct(DOWN)

    def left(self):
        self.direct(LEFT)

    def right(self):
        self.direct(RIGHT)

    def extend(self):
        self.segments.append(SnakeSegment(self.tail.pos()))

class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.move()

    def move(self):
        self.setpos(x=randint(-250, 250),y=randint(-250, 250))