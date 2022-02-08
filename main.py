from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("PONG GAME")
screen.tracer(0)

ball = Ball()
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
s = Score()

screen.listen()
screen.onkey(paddle_r.up,'Up')
screen.onkey(paddle_r.down,'Down')
screen.onkey(paddle_l.up,'w')
screen.onkey(paddle_l.down,'s')

speed_begin = 1
game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()< -320:

        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        s.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        s.r_point()

screen.exitonclick()
