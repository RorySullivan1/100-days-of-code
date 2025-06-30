import turtle
from turtle import Turtle, Screen
from random import randint

def random_color():
    rgb_list = []
    for _ in range(3):
        rgb_list.append(randint(0,255))
    return tuple(rgb_list)


class Racer:
    def __init__(self, id: int, color: str = None):
        self.core = Turtle()
        self.id = id
        color = random_color() if not color else color
        turtle.colormode(255)
        self.core.color(color)
        self.core.penup()
        self.core.shape("turtle")
        ...

    def move(self, speed: str | int = "random"):
        if speed == "random":
            return self.core.forward(randint(1,30))
        else:
            return self.core.forward(int(speed))


class Race:
    turtle.hideturtle()
    def __init__(self):
        self.screen = Screen()
        self.racers = self.get_racers()
        self.winner = None
        self.racer_count = 0
        self.run_race()

    @staticmethod
    def get_racers():
        racers = []
        for x in range(10):
            racers.append(Racer(id=x+1))
        return racers

    def move_racers(self):
        for racer in self.racers:
            racer.move()

    def check_winner(self):
        for racer in self.racers:
            if racer.core.pos()[0] >= 300:
                self.winner = racer

    def reset_racers(self):
        turtle.clear()
        positions = [x * 50 for x in range(-5, 5)]
        for racer in self.racers:
            position = positions.pop()
            racer.core.goto(-300, position)

    def announce_winner(self):
        ...

    def run_race(self):
        self.reset_racers()
        self.screen.textinput("Place your bets!", "Pick your racer! (By number)")
        while not self.winner:
            self.move_racers()
            self.check_winner()
        self.winner.core.write(f"Turtle #{self.winner.id} Wins!)", align="right")
        self.screen.exitonclick()

Race()




