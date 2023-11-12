from turtle import Screen, Turtle
from math import sqrt
from random import randint
WIDTH, HEIGHT = 780, 630
SMALL_FONT = ('Arial', 25, 'normal')
LARGE_FONT_SIZE = 70
LARGE_FONT = ('Arial', LARGE_FONT_SIZE, 'normal')
def forward():
    player1.fd(speed1)
    player2.fd(speed2)
def turn_right():
    player1.rt(45)
def turn_left():
    player1.lt(45)
def turn_right2():
    player2.rt(45)
def turn_left2():
    player2.lt(45)
def button_click(x, y):
    if -150 < x < 150 and -100 < y < 0:
        exit()
def exit_button():
    button.begin_fill()
    for _ in range(2):
        button.forward(300)
        button.left(90)
        button.forward(100)
        button.left(90)
    button.end_fill()
    button_text.write("Exit", align='center', font=LARGE_FONT)
    screen.onscreenclick(button_click)
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('#202020')
screen.title("SpaceWar")
border = Turtle()
border.hideturtle()
border.color('white')
border.speed('fastest')
border.pensize(3)
border.penup()
border.setposition(15 - WIDTH/2 - 4, 15 - HEIGHT/2 + 4)  # 4 = adjustment for "chrome"
border.pendown()
for side in range(2):
    border.forward(WIDTH - 30)
    border.left(90)
    border.forward(HEIGHT - 30)
    border.left(90)
score = 0
text2 = Turtle()
text2.hideturtle()
text2.color('white')
text2.penup()
text2.setposition(70, 200)
scorestring = "Score: %s" % score
text2.write(scorestring, align='center', font=SMALL_FONT)
text3 = Turtle()
text3.hideturtle()
text3.color('red')
button = Turtle()
button.hideturtle()
button.color('white')
button.speed('fastest')
button.pensize(4)
button.penup()
button.goto(-150, -100)
button_text = Turtle()
button_text.hideturtle()
button_text.penup()
button_text.goto(0, -50 + -LARGE_FONT_SIZE/2)
booster1 = Turtle()
booster1.shape('circle')
booster1.color('#1c77d9')
booster1.speed('fastest')
booster1.penup()
booster1.setposition(randint(-250, 250), randint(-250, 250))
booster2 = Turtle()
booster2.shape('circle')
booster2.color('#d6281c')
booster2.speed('fastest')
booster2.penup()
booster2.setposition(randint(-250, 250), randint(-250, 250))
decreaser = Turtle()
decreaser.shape('circle')
decreaser.color('green')
decreaser.speed('fastest')
decreaser.penup()
decreaser.setposition(randint(-250, 250), randint(-250, 250))
speed1 = 3
speed2 = 3
player1 = Turtle()
player1.shape('triangle')
player1.color('#1c77d9')
player1.shapesize(1.5)
player1.speed('fastest')
player1.penup()
player1.setx(-330)
player2 = Turtle()
player2.shape('triangle')
player2.color('#d6281c')
player2.shapesize(1.5)
player2.speed('fastest')
player2.penup()
player2.setheading(180)
player2.setx(330)
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkey(turn_left2, 'Left')
screen.onkey(turn_right2, 'Right')
screen.listen()
while True:
    forward()
    a = sqrt(pow(player1.xcor() - player2.xcor(), 2) + pow(player1.ycor() - player2.ycor(), 2))
    b = sqrt(pow(player1.xcor() - booster1.xcor(), 2) + pow(player1.ycor() - booster1.ycor(), 2))
    c = sqrt(pow(player2.xcor() - booster2.xcor(), 2) + pow(player2.ycor() - booster2.ycor(), 2))
    d = sqrt(pow(player1.xcor() - decreaser.xcor(), 2) + pow(player1.ycor() - decreaser.ycor(), 2))
    e = sqrt(pow(player2.xcor() - decreaser.xcor(), 2) + pow(player2.ycor() - decreaser.ycor(), 2))
    if a < 20:
        player1.setx(-330)
        player1.setheading(0)
        player2.setx(330)
        player2.setheading(180)
        score += 1
        text2.undo()
        scorestring = "Score: %s" % score
        text2.write(scorestring, align='center', font=SMALL_FONT)
    if b < 20:
        speed1 += 1
        booster1.setposition(randint(-250, 250), randint(-250, 250))
    if c < 20:
        speed2 += 1
        booster2.setposition(randint(-250, 250), randint(-250, 250))
    if d < 20:
        speed1 -= 1
        decreaser.setposition(randint(-250, 250), randint(-250, 250))
    if e < 20:
        speed2 -= 1
        decreaser.setposition(randint(-250, 250), randint(-250, 250))
    if speed1 == 7:
        speed1 -= 1
    if speed2 == 7:
        speed2 -= 1
    if not -375 <= player1.xcor() <= 375:
        score += 1
        player1.setx(-330)
        player1.setheading(0)
        text2.undo()
        scorestring = "Score: %s" % score
        text2.write(scorestring, align='center', font=SMALL_FONT)
    if not -300 <= player1.ycor() <= 300:
        score += 1
        player1.setx(-330)
        player1.setheading(0)
        text2.undo()
        scorestring = "Score: %s" % score
        text2.write(scorestring, align='center', font=SMALL_FONT)
    if not -375 <= player2.xcor() <= 375:
        player2.right(180)
    if not -300 <= player2.ycor() <= 300:
        player2.right(180)
    if score == 2:
        text3.write("Red Won!", align='center', font=LARGE_FONT)
        booster1.hideturtle()
        booster2.hideturtle()
        decreaser.hideturtle()
        player1.hideturtle()
        player2.hideturtle()
        exit_button()
        break
screen.mainloop()
