from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        """
        Initializes the ball with a specific shape, color, and speed. 
        The ball starts in the center of the screen and then moves in a random direction.
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
        Sets the ball's heading to a random direction from a set of possible angles.
        """
        angle = random.choice([45, 135, 225, 315])
        self.setheading(angle)

    def move(self):
        """
        Moves the ball by updating its position based on current x and y movement.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the ball's y-axis movement to simulate bouncing off a horizontal surface.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's x-axis movement and increases the speed to simulate bouncing off a paddle.
        """
        self.x_move *= -1
        self.move_speed *= 0.9  #ball goes faster when touching paddles

    def reset_position(self):
        """
        Resets the ball to the center of the screen and reduces its speed. 
        The ball then moves in the opposite direction of its previous movement.
        """
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
