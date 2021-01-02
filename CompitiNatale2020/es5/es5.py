'''
es5:
Scrivere uno snake in python utilizzando la libreria turtle

Andrea Tomatis
'''

import turtle
import random

snake = turtle.Turtle()
snake.resizemode("user")
snake.shapesize(2.5, 2.5, 3)

win = turtle.Screen()

mela = turtle.Turtle()
mela.hideturtle()
width = 800
height = 600
win.setup(width=width, height=height)
win.title("Snake")
win.bgcolor("green")

win.register_shape("mela.gif")
mela.shape("mela.gif")
mela.up()
snake.pencolor("blue")


punti = 0


def left():
    snake.setheading(180)
    snake.setx(snake.xcor() - 10)
    if snake.xcor() < (width/2-20) * -1:
        win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
                     False, align="center", font=("Arial", 30, "normal"))
    controllaMela()


def right():
    snake.setheading(0)
    snake.setx(snake.xcor() + 10)
    if snake.xcor() > (width/2-20):
        win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
                     False, align="center", font=("Arial", 30, "normal"))
    controllaMela()


def up():
	snake.setheading(90)
	snake.sety(snake.ycor() + 10)
	if snake.ycor() > height/2-20:
		win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",False, align="center", font=("Arial", 30, "normal"))
	controllaMela()


def down():
	snake.setheading(270)
	snake.sety(snake.ycor() - 10)
	if snake.ycor() < (height/2-20) * -1:
		win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
                     False, align="center", font=("Arial", 30, "normal"))
	controllaMela()


def controllaMela():
	if snake.pos() == mela.pos():
		aggiungiMela(width, height)
		global punti
		punti += 1


def aggiungiMela(width, height):
	x = random.randint(width/2 * -1, width/2)//10 * 10
	y = random.randint(height/2 * -1, height/2)//10 * 10
	mela.hideturtle()
	mela.setx(x)
	mela.sety(y)
	mela.showturtle()


def disegnaQuadrato():
	snake.begin_fill()
	for i in range(4):
		snake.forward(15)
		snake.left(90)
	snake.end_fill()


def muovi():
	snake.forward(10)


aggiungiMela(width, height)

win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(up, "Up")
win.onkey(down, "Down")
win.listen()
win.mainloop()

print(f"Hai perso: hai totalizzato {punti} punti")
