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
        self.shapesize(stretch_wid=6, stretch_len=1)  #changes shape of paddle
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        Moves the paddle upward by increasing its y-coordinate.
        Ensures that the paddle doesn't move beyond the top of the screen.
        """
        new_y = self.ycor() + 20  #move up
        if new_y < 260:  #so it cant go above the "roof"
            self.goto(self.xcor(), new_y)  

    def go_down(self):
        """
        Moves the paddle downward by decreasing its y-coordinate.
        Ensures that the paddle doesn't move beyond the bottom of the screen.
        """
        new_y = self.ycor() - 20  
        if new_y > -240:  
            self.goto(self.xcor(), new_y)  
