from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        """
        creates the ball with a specific shape, color, and speed. 
        ball starts in the middle and then goes a random direction
        """
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.set_random_direction()

    def set_random_direction(self):
        """
        sets the random direction the ball will go out of the presets : 45, 135, 225, 315
        """
        angle = random.choice([45, 135, 225, 315])
        self.setheading(angle)

    def move(self):
        """
        moves the ball by updating its x and y position respectively
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        makes ball reverse direction as if it "bounced" off the roof
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        makes the ball reverse direction as if it "bounced" off the walls
        """
        self.x_move *= -1
        self.move_speed *= 0.9  #ball goes faster when touching paddles

    def reset_position(self):
        """
        after the ball "dies" it respawns in the middle of the screen with reset movespeed 
        """
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
