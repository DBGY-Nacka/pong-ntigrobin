from turtle import Turtle
import time  # for the timer

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")
POSITION = (0, 260)
TIMER_FONT = ("Courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self, player1: str = "Player 1", player2: str = "Player 2"):
        """
        starts scoreboard with player names, scores, time.

        Args:
            player1 (str): name of the player 1 or "player 1" by default.
            player2 (str): name of the player 2 or "player 2" by default.
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
        used to update the scoreboard
        """
        self.clear()
        self.goto(-200, 260)  #left player's score
        self.write(f"{self.player1}:{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)   #right player's score
        self.write(f"{self.player2}:{self.r_score}", align=ALIGNMENT, font=FONT)
        self.show_time()

    def show_time(self):
        """
        shows the game time in the middle and a little below the names
        """
        time_spent = int(time.time() - self.start_time)
        self.goto(0, 200)
        self.write(f"{time_spent}", align=ALIGNMENT, font=TIMER_FONT)

    def l_point(self):
        """
        gives a point to left player (player 1) and updates the scoreboard
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        gives a point to right player (player 2) and updates the scoreboard
        """
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, winner: str):
        """
        shows game over screen with winner text in the middle
        
        Args:
            winner (str): The name of the player who won the game.
        """
        self.goto(0, 75)
        self.write(f"{winner} wins!", align=ALIGNMENT, font=FONT)
