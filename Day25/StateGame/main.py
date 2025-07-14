import turtle
from turtle import Screen, Turtle
import pandas as pd

class StateGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("U.S. States Games")
        self.screen.tracer(0)
        states_image = "blank_states_img.gif"
        self.screen.addshape(states_image)
        self.screen.bgpic(states_image)
        self.data = self.read_states()
        self.states_upper = [state.title() for state in self.data["state"].tolist()]
        self.state_count = len(self.states_upper)
        self.states_named = 0
        self.game_on = True
        self.play()

    @staticmethod
    def read_states():
        return pd.read_csv("50_states.csv")

    def get_guess(self):
        guess = self.screen.textinput(
            title=f"{self.states_named}/50 States Found!",
            prompt="Guess the Missing States' Names!")
        if not guess:
            self.game_over()
            self.game_on = False
            self.screen.bye()
        else:
            guess = guess.title()
        if guess in self.states_upper:
            self.states_upper.remove(guess)
            self.plot_state(guess)
            self.states_named += 1


    def game_over(self):
        pd.DataFrame(
            {"Missed States": self.states_upper}
        ).to_csv("./missed_states.csv")

    def plot_state(self, state: str):
        writing = Turtle()
        writing.hideturtle()
        writing.penup()
        writing.color("black")
        state_data = self.data[self.data["state"] == state]
        writing.setpos(state_data.x.values[0], state_data.y.values[0])
        writing.write(state_data.state.values[0], align="center", font=("Source Sans Pro", 12, "bold"))

    def play(self):
        while self.game_on:
            self.get_guess()
            self.screen.update()
            if self.states_named == self.state_count:
                self.game_on = False

        self.screen.mainloop()




StateGame()

