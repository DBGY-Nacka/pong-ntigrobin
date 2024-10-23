from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """
        creates a Paddle object, inheriting from the Turtle class.
        paddle is set to a rectangular (square) shape (6 units tall and 1 unit wide) and positioned at the specified coordinates
        
        Args:
            position: (x, y) coordinates where the paddle should be placed on the screen
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=0.5)  #changes shape of paddle
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        moves the paddle up by increasing y-cord while making sure it doesn't go into the "roof"
        """
        new_y = self.ycor() + 20  #move up
        if new_y < 260:  #so it cant go above the "roof"
            self.goto(self.xcor(), new_y)  

    def go_down(self):
        """
        moves the paddle down by decreasing y-cord while making sure it doesn't go into the "floor"
        """
        new_y = self.ycor() - 20  
        if new_y > -240:  
            self.goto(self.xcor(), new_y)  
