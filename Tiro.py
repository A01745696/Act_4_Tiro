"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""
#Codigo modificado por:
#Autor: Yahir Cortes Rodriguez
#Autor: Fabrizio González Servín

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):

    """
    [Respond to screen tap]
    :parameter start: [Values of the first click in x and y]
    :parameter ends: [Values of the direction and speed in x and y]
    """

    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Se aumentan los valores sumados a x y y, respectivamente para aumentar la velocidad de la pelota
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25

def inside(xy):
    """
    [Return True if xy within screen]
    :parameter start: [Values of the first click in x and y]
    :parameter ends: [True or False]
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """
    [Por cada target se dibuja un punto azul y para cuando la pelota esta en el rango se dibuja de color rojo]
    """
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """
    [En esta funcion se define el la velicidad con la que retorceden los targets,
    se hace el efecto parabolico restandole velocidad a la bola en y,
    se regresa el target si llega al final de la pantalla]
    """
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.8         # Se aumenta el valor para aumentar la velocidad de los balones

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            #Si el target no esta en la pantalla se regresa al final en x y su posicion en y se randomiza
            target.x=200
            target.y=randrange(-200,201)

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
