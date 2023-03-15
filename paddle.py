from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position: int, y_position: int):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, y_position)

    def go_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), new_y_position)

    def go_down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.xcor(), new_y_position)
