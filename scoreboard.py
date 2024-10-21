from turtle import Turtle
import time  # for the timer

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
POSITION = (0, 260)
TIMER_FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self, player1: str = "Player 1", player2: str = "Player 2"):
        """
        Initializes the scoreboard with player names, colors, scores, and starting time.

        Args:
            player1 (str): Name of the first player.
            player2 (str): Name of the second player.
        """
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # l = left player score
        self.r_score = 0  # r = right player score
        self.start_time = time.time()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current score for both players and displays the timer.
        """
        self.clear()
        self.goto(-100, 260)  #left player's score
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)   #right player's score
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.show_time()

    def show_time(self):
        """
        Displays the time elapsed in the middle of the screen.
        """
        time_spent = int(time.time() - self.start_time)
        self.goto(0, 200)
        self.write(f"{time_spent}", align=ALIGNMENT, font=TIMER_FONT)

    def l_point(self):
        """
        Increments the score of the left player by 1 and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increments the score of the right player by 1 and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, winner: str):
        """
        Displays the game over message with the name of the winner.

        Args:
            winner (str): The name of the player who won the game.
        """
        self.goto(0, 75)
        self.write(f"{winner} wins!", align=ALIGNMENT, font=FONT)
