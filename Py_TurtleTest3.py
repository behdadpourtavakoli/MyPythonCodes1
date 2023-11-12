from turtle import Screen, Turtle
import time
import turtle
is_game_on = False
# is_game_on = True

def click(i, j):
    global is_game_on
    if i >= 250 and j >= 300:
        is_game_on = True
        print(is_game_on)
        while is_game_on:
            time.sleep(0)
            screen.update()
            ball.move()
            if ball.ycor() >= 375:
                ball.bounce_y()
            if (abs(ball.xcor() - paddle.xcor()) < 120) and ball.ycor() == -355:
                ball.bounce_y()
    return is_game_on

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.speed(6)
        self.goto(0, -355)
        self.x_move = 0
        self.y_move = 1
        self.move_speed = 10
    def move(self):
        xcor_new = self.xcor() + self.x_move
        ycor_new = self.ycor() + self.y_move
        self.goto(xcor_new, ycor_new)
    def bounce_y(self):
        self.y_move *= -1

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.goto(0, -380)
        self.color('blue')
        self.shapesize(stretch_wid=.5, stretch_len=10)
    def move(self,i, j):
        self.goto(i,  -380)

class Start(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(250, 300)
        self.color('blue')
        self.shapesize(stretch_wid=4, stretch_len=10)
        self.hideturtle()
        self.write('Click to Start', font=('Arial', 35, 'bold'))

screen = Screen()
screen.colormode(255)
screen.bgcolor('white')
screen.setup(1200, 800)
screen.tracer(0)
paddle = Paddle()
ball = Ball()
screen.listen()
paddle.ondrag(paddle.move)
screen.onclick(click)
start = Start()
screen.update()
turtle.done()
screen.exitonclick()
