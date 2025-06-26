import turtle
from turtle import Turtle, Screen


def draw_colorful_pinwheel():
    timmy = Turtle()
    screen = Screen()
    for step in range(100):
        for c in ("blue", "red", "green"):
            timmy.color(c)
            timmy.forward(step)
            timmy.right(10)

    screen.exitonclick()

def draw_square():
    cursor = Turtle()
    screen = Screen()

    for _ in range(4):
        cursor.forward(100)
        cursor.right(90)

    screen.exitonclick()

def draw_dotted():
    cursor = Turtle()
    screen = Screen()

    for _ in range(50):
        cursor.forward(10)
        cursor.penup()
        cursor.forward(10)
        cursor.pendown()

    screen.exitonclick()

def draw_multiple_shape():
    import random
    cursor = Turtle()
    screen = Screen()

    for sides in range(3,10):
        color = random.choice(["blue", "red", "green", "yellow", "orange", "purple"])
        cursor.color(color)
        for side in range(1, sides + 1):
            cursor.forward(100)
            cursor.right(360/sides)

    screen.exitonclick()


def draw_random_walk():
    import random
    cursor = Turtle()
    screen = Screen()

    cursor.pensize(10)
    cursor.speed(20)
    turtle.colormode(255)
    for _ in range(1000):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        cursor.color(color)
        direction = random.randint(0,360)
        cursor.setheading(direction)
        size = random.randint(0, 100)
        cursor.forward(size)

    screen.exitonclick()

def draw_spirograph():
    import random
    cursor = Turtle()
    screen = Screen()

    cursor.pensize(1)
    cursor.speed(1)
    turtle.colormode(255)
    screen.tracer(0)

    frames = 40
    for x in range(1, frames):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cursor.color(color)
        cursor.setheading(360-x*(360/frames))
        for y in range(360):
            cursor.forward(1)
            cursor.right(1)
        screen.update()

    screen.exitonclick()

def create_hirst_dot_painting():
    cursor = Turtle()
    screen = Screen()

    import colorgram
    import random
    colors = colorgram.extract("hirst_dot_painting.jpg", 20)
    print(colors)
    cursor.speed(0)
    turtle.colormode(255)

    for y in range(-500, 500, 50):
        for x in range(-500, 500, 50):
            cursor.color(random.choice(colors).rgb)
            cursor.teleport(x,y)
            cursor.begin_fill()
            cursor.circle(10)
            cursor.end_fill()


    screen.exitonclick()

create_hirst_dot_painting()

