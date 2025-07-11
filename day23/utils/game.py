from turtle import Screen, Turtle

DEFAULT_GAMESIZE = {"width": 1000, "height": 500}


class Game:
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(**DEFAULT_GAMESIZE)
        self._screen.bgcolor("white")
        self._screen.title("Turtle Game")
        self._screen.tracer(0)
        self._game_on = False

    def _start_game(self):
        self._game_on = True

    def run(self):
        self._start_game()

        while self._game_on:
            ...

        self._screen.exitonclick()
