from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

def move_forward():
    cursor.forward(10)
    ...

def move_backward():
    cursor.backward(10)
    ...

def turn_right():
    cursor.setheading(to_angle=cursor.heading()+5)

def turn_left():
    cursor.setheading(to_angle=cursor.heading()-5)

screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=cursor.clear,key="c")
screen.exitonclick()
