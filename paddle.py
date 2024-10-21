from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """
        Initializes a Paddle object, inheriting from the Turtle class.
        The paddle is set to a rectangular shape (6 units tall and 1 unit wide) and positioned at the specified coordinates.
        
        Args:
            position (tuple): The (x, y) coordinates where the paddle should be placed on the screen.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)  # Makes the paddle long and narrow
        self.penup()
        self.goto(position)  # Position the paddle at the specified location

    def go_up(self):
        """
        Moves the paddle upward by increasing its y-coordinate.
        Ensures that the paddle doesn't move beyond the top of the screen.
        """
        new_y = self.ycor() + 20  # Increase y-coordinate by 20 units
        if new_y < 260:  # Restrict the paddle from moving above the top boundary
            self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def go_down(self):
        """
        Moves the paddle downward by decreasing its y-coordinate.
        Ensures that the paddle doesn't move beyond the bottom of the screen.
        """
        new_y = self.ycor() - 20  # Decrease y-coordinate by 20 units
        if new_y > -240:  # Restrict the paddle from moving below the bottom boundary
            self.goto(self.xcor(), new_y)  # Move the paddle to the new position
