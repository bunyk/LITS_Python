
import turtle
import random

def tree(h):
    if h < 7:
        return

    turtle.up()
    turtle.forward(h)

    left = 20 + random.random() * 25
    right = 20 + random.random() * 25
    turtle.left(left)
    tree(h / (1.1 + random.random() / 3))

    turtle.right(left + right)
    tree(h / (1.1 + random.random() / 3))
    turtle.left(right)

    if h < 14:
        turtle.color('green')
        turtle.pensize(2 + 20 / h)
    else:
        turtle.color('brown')
        turtle.pensize(h / 5)

    turtle.down()
    turtle.back(h)

turtle.speed(0)

turtle.up()
turtle.back(200)
turtle.left(90)
turtle.back(200)
tree(70)

turtle.up()
turtle.right(90)
turtle.forward(400)
turtle.left(90)
tree(70)

input()
