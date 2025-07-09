from turtle import Turtle, Screen
from time import sleep
from day21.core.objects import Player, PongBall, Scoreboard

GAME_TITLE = "PONG"
CPU_LEVEL = "RANDOM"
CPU_COLOR = "Red"
PLAYER_COLOR = "Blue"
SCREEN_SIZE = {"width": 800,
               "height": 600}
SCREEN_BACKGROUND_COLOR = "Black"

class Pong:
    def __init__(self):
        self._init_field()
        self._init_objects(cpu_level=CPU_LEVEL)
        self._call_scoreboard()
        self._active_game()
        self.game_on = False
        self.play()

    def _init_field(self):
        """Establishes Field of Pong"""
        scrn = Screen()
        scrn.title(GAME_TITLE)
        scrn.setup(**SCREEN_SIZE)
        scrn.bgcolor(SCREEN_BACKGROUND_COLOR)
        scrn.tracer(0)
        self.screen = scrn

        self._draw_midline()

    def _init_objects(self, cpu_level: str):
        self.pongball = PongBall()
        self.player1 = Player(name="1", color=PLAYER_COLOR, pos=(-350, 0))
        self.player2 = Player(name="2", color=CPU_COLOR, pos=(350, 0))
        self.scoreboard = ""
        ...

    def _active_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.player1.move_up, "w")
        self.screen.onkeypress(self.player1.move_down, "s")
        self.screen.onkeypress(self.player2.move_up, "Up")
        self.screen.onkeypress(self.player2.move_down, "Down")
        self.screen.onkey(self.game_start,"space")

    def _call_scoreboard(self):
        self.player_1_score = Scoreboard(player=self.player1, pos=(-50, 200))
        self.player_2_score = Scoreboard(player=self.player2, pos=(50, 200))

    def _draw_midline(self):
        mid_line = Turtle()
        mid_line.shape("square")
        mid_line.hideturtle()
        mid_line.penup()
        mid_line.setpos(0,SCREEN_SIZE["height"]/2)
        mid_line.setheading(270)
        mid_line.pensize(5)
        mid_line.pencolor("white")
        for _ in range(0, int(SCREEN_SIZE["height"]/40)):
            mid_line.pendown()
            mid_line.forward(20)
            mid_line.penup()
            mid_line.forward(20)
        self.midline = mid_line

    def get_winner(self):
        winner_name = max(self.player_1_score,
                          self.player_2_score,
                          key=lambda p: p.score).player.name
        return winner_name

    def game_over(self):
        self.game_on = False
        self.midline.clear()
        winner = self.get_winner()
        game_over_sign = Turtle()
        game_over_sign.hideturtle()
        game_over_sign.setpos(0,0)
        game_over_sign.color("white")
        game_over_sign.write(f"GAME OVER\nPlayer #{winner} Wins!",
                             align="center",
                             font=("Courier", 20, "bold"))

    def detect_collisions(self):
        # Redirect at top / bottom walls
        if self.pongball.ycor() > 280 or self.pongball.ycor() < -280:
            self.pongball.bounce_y()

        #Redirect if collision with Paddle
        if self.pongball.distance(self.player1) < 50 and self.pongball.xcor() < self.player1.xcor() + 30:
            self.pongball.bounce_x()

        # Redirect if collision with Paddle
        if self.pongball.distance(self.player2) < 50 and self.pongball.xcor() > self.player2.xcor() - 30:
            self.pongball.bounce_x()

        #Scoring
        if self.pongball.xcor() > 380:
            self.player_1_score.add_score(1)
            self.pongball.reset_ball()

        if self.pongball.xcor() < -380:
            self.player_2_score.add_score(1)
            self.pongball.reset_ball()

        if self.player_1_score.score > 5 or self.player_2_score.score > 5:
            self.game_over()


    def game_start(self):
        self.game_on = True

    def play(self):

        while not self.game_on:
            self.screen.update()
            sleep(0.1)

        self.pongball.launch()
        while self.game_on:
            self.screen.update()
            self.detect_collisions()
            self.pongball.move()
            sleep(0.05)

        self.screen.exitonclick()

