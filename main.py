from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player1 = screen.textinput("Player 1", "Enter your name:") or "Player 1"
player2 = screen.textinput("Player 2", "Enter your name:") or "Player 2"

r_paddle = Paddle((350, 0))  
l_paddle = Paddle((-350, 0)) 
ball = Ball()
scoreboard = Scoreboard(player1, player2)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    scoreboard.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280: #ball bounce against wall/floor
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

        if scoreboard.l_score >= 10:
            scoreboard.game_over(f" {player1} WINS")
            game_is_on = False

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

        if scoreboard.r_score >= 10:
            scoreboard.game_over(f"{player2} WINS")
            game_is_on = False

screen.textinput("Game Over", "Press Enter to exit.") #to show the text box before closing the game
screen.bye()