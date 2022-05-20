from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")


def test():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


test()