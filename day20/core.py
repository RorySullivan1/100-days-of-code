from turtle import Screen
from objects import Snake, SnakeFood, ScoreBoard
from time import sleep

COLLISION_SENSITIVITY = 15
BOUNDARIES = [-290, 290]
EDGE_BUFFER = 15

class SnakeGame:
    def __init__(self):
        self._init_screen()
        self._init_objects()
        self._init_listen()
        self.run_game()

    def _init_objects(self):
        self.snake = Snake()
        self.food = SnakeFood()
        self.scoreboard = ScoreBoard()

    def _init_screen(self):
        screen = Screen()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        self.screen = screen

    def _init_listen(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")

    def check_collisions(self):
        snake_head = self.snake.head
        if snake_head.distance(self.food) < COLLISION_SENSITIVITY:
            self.food.move()
            self.snake.extend()
            self.scoreboard.update(1)
        if snake_head.xcor() < BOUNDARIES[0] or snake_head.xcor() > BOUNDARIES[1]:
            return False
        elif snake_head.ycor() < BOUNDARIES[0] or snake_head.ycor() > BOUNDARIES[1]:
            return False

        for seg in self.snake.segments[1:]:
            if snake_head.distance(seg) < 10:
                return False

        return True

    def run_game(self):
        game_on = True

        while game_on:
            self.screen.update()
            self.snake.move()
            game_on = self.check_collisions()
            sleep(0.1)

        self.scoreboard.game_over()
        self.screen.exitonclick()