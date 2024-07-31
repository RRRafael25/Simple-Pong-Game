import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball_speed = 0.1
ball_direction_y = 1
ball_direction_x = 1

ball.dx = ball_speed * ball_direction_x
ball.dy = ball_speed * ball_direction_y
#Score
max_score = 7
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
pen_score = turtle.Turtle()
pen_score.speed(0)
pen_score.color("white")
pen_score.penup()
pen_score.hideturtle()
pen_score.goto(0,220)

#functions for the game
def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)
def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)
    
def border_up(paddle):
    y = paddle.ycor()
    if y < 245:
        paddle_up(paddle)
def border_down(paddle):
    y = paddle.ycor()
    if y > -240:
        paddle_down(paddle)


def score():
    if (score_a > score_b):
        pen.clear()
        pen.write("Player A Wins", align="center", font=("Courier", 24, "normal"))
    else:
        pen.clear()
        pen.write("Player B Wins", align="center", font=("Courier", 24, "normal"))
def restart():
    global score_a
    global score_b
    if (score_a ==  max_score or score_b == max_score):
            score_a = 0
            score_b = 0
            pen.clear()
            pen_score.clear()
            pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
            pen_score.write(" ", align="center", font=("Courier", 24, "normal"))
#Keyboard binding
wn.listen()
wn.onkeypress(lambda: border_up(paddle_a), "w")


wn.onkeypress(lambda: border_up(paddle_b), "Up")

wn.onkeypress(lambda: border_down(paddle_a), "s")
wn.onkeypress(lambda: border_down(paddle_b), "Down")
wn.onkeypress(lambda: restart(), " ")
wn.onkeypress(wn.bye, "Escape")
#Main game loop
while True:
    wn.update() 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball_direction_y *= -1
        ball.dy = ball_speed * ball_direction_y
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_direction_y *= -1
        ball.dy = ball_speed * ball_direction_y
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball_direction_x *= -1
        ball_speed = 0.1
        ball.dx = ball_speed * ball_direction_x
        score_a += 1
        ball.goto(0,0)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball_direction_x *= -1
        ball_speed = 0.1
        ball.dx = ball_speed * ball_direction_x
        score_b += 1
        ball.goto(0,0)
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "normal"))
    
    #Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball_direction_x *= -1
        ball_speed += 0.02
        ball.dx = ball_speed * ball_direction_x
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball_direction_x *= -1
        ball_speed += 0.02
        ball.dx = ball_speed * ball_direction_x
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        
    if (score_a ==  max_score or score_b == max_score):
        score()
        ball.goto(0,0)
        ball_speed = 0.1
        ball.dx = ball_speed * ball_direction_x
        pen_score.write("Press Space to restart", align="center", font=("Courier", 24, "normal"))
        