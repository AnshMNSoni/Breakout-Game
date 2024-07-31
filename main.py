from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random, time, turtle


box_lst = []

screen = Screen()
screen.tracer(0)

screen.bgcolor('black')
screen.title('Breakout Game')
screen.setup(width=1000, height=650)


paddle = Paddle()


def random_clr():
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tpl = (r, g, b)
    return tpl


tut_down = True
tut_left = True


X = -490
Y = 290

while tut_down:
    while tut_left:
        tut = Turtle('square')
        tut.penup()
        tut.shapesize(stretch_len=7.5, stretch_wid=2.5)
        tut.color(random_clr())
        tut.goto(x=X, y=Y)
        box_lst.append(tut)
        X += 160

        if X >= 480:
            tut_left = False

    X = -490   
    Y -= 60
    tut_left = True

    if Y <= -100:
        tut_down = False


screen.update()


screen.listen()
screen.onkey(key='Left', fun=paddle.on_left)
screen.onkey(key='Right', fun=paddle.on_right)


ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()


    # Detect collision with wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.x_bounce()

    if ball.ycor() > 320:
        ball.y_bounce()
        
           
    # Detect collision with paddle
    for seg in paddle.segments:
        if ball.distance(seg) < 25 and ball.ycor() < -270:
            ball.y_bounce()


    # Detect collision with bricks
    for box in box_lst:
        if ball.distance(box) < 60:
            ball.y_bounce()
            box.goto(2000, 2000)  # Move the box off-screen
            box_lst.remove(box)


    # Reset ball position if it goes out of bounds
    if ball.ycor() < -320:
        ball.reset_position()


    screen.update()

screen.exitonclick()
