from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.ball_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x_coordinate = self.xcor() + self.x_move
        new_y_coordinate = self.ycor() + self.y_move
        self.goto(new_x_coordinate, new_y_coordinate)

    def bounce_y_axis(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x_axis(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x_axis()

