from turtle import Turtle, Screen
from random import randint
from time import sleep

FIELD_BOUNDARIES = [-290, 290]
FIELD_SIZE = (600, 600)
COLLISION_SENSITIVITY = 15
SNAKE_STARTING_POS = [(0, 0), (-20, 0), (-40,0)]
SNAKE_SPEED = 20
SNAKE_DIRECTION = {"up": 90, "down": 270, "left": 180, "right": 0}
SCOREBOARD_POSITION = (0, 240)
SCOREBOARD_FONT = ("Courier", 24, "bold")
SCOREBOARD_ALIGNMENT = "center"
HIGHSCORE_FILE = "/highscore.txt"


class Game:
    def __init__(self):
        self.screen = self.set_screen()
        self.snake = Snake()
        self.food = SnakeFood()
        self.scoreboard = ScoreBoard()
        self.listen()
        self.run()

    @staticmethod
    def set_screen():
        screen = Screen()
        screen.setup(FIELD_SIZE[0], FIELD_SIZE[1])
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        return screen

    def listen(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def refresh(self, refresh_time: float):
        self.screen.update()
        sleep(refresh_time)

    def exit_on_click(self):
        self.screen.exitonclick()

    def check_collisions(self):
        snake_head = self.snake.head
        if snake_head.distance(self.food) < COLLISION_SENSITIVITY:
            self.food.move()
            self.snake.extend()
            self.scoreboard.update(1)
        if snake_head.xcor() < FIELD_BOUNDARIES[0] or snake_head.xcor() > FIELD_BOUNDARIES[1]:
            return False
        elif snake_head.ycor() < FIELD_BOUNDARIES[0] or snake_head.ycor() > FIELD_BOUNDARIES[1]:
            return False

        for seg in self.snake.segments[1:]:
            if snake_head.distance(seg) < 10:
                return False
        return True

    def run(self):
        game_on = True
        while game_on:
            self.screen.update()
            self.snake.move()
            game_on = self.check_collisions()
            sleep(0.1)
        if self.scoreboard.score > self.scoreboard.highscore:
            self.scoreboard.write_highscore()
        self.scoreboard.game_over()
        self.screen.exitonclick()

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

class Snake:
    def __init__(self):
        self.segments = [SnakeSegment(cord) for cord in SNAKE_STARTING_POS]

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
        self.head.forward(SNAKE_SPEED)

    def direct(self, key: str):
        if not abs(180 - self.head.heading()) == SNAKE_DIRECTION[key]:
            self.head.setheading(SNAKE_DIRECTION[key])

    def up(self):
        self.direct("up")

    def down(self):
        self.direct("down")

    def left(self):
        self.direct("left")

    def right(self):
        self.direct("right")

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

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(SCOREBOARD_POSITION)
        self.display()

    def read_highscore(self):
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())

    def write_highscore(self):
        with open(HIGHSCORE_FILE, "w") as file:
            file.write(str(self.score))

    def display(self):
        self.write(f"Score: {self.score} | Highscore: {self.highscore}",
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