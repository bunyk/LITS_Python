import turtle;

import random;

LEFT = 36

def tree(h, n):


    if n < 8: 
        turtle.color('brown')
        turtle.pensize(10 - n)
    else:
        turtle.pensize(5)
        turtle.color('green')

    if n < 10:
        turtle.forward(h)

        turtle.left(LEFT)

        turtle.color('green')
        tree(h / 1.29+random.random(), n + 1)

        angle = 10 + random.random() * 50
        turtle.right(angle)

        tree(h / 1.3, n + 1)


        turtle.left(angle - LEFT)

        turtle.up()

        turtle.back(h + 1)

        turtle.down()

turtle.speed(0)
turtle.left(90)

tree(100, 0)

input('Press Enter to continue')
