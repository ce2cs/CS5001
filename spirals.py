import math
import turtle


def main():
    """
    draw a spiral picture with turtle
    :return: None
    """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i in range(20, 200):
        t.lt(10)
        drop(t, i, 'blue')
    for i in range(100, 300, 2):
        t.lt(10)
        triangle(t, i, 'green')
    for i in range(100, 400, 3):
        t.lt(10)
        diamond(t, i, 'red')
    turtle.exitonclick()


def triangle(t, size, color):
    """
    draw a triangle
    :param t: turtle object
    :param size: integer
    :param color: pen color
    :return:
    """
    t.pd()
    t.color(color)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.pu()


def diamond(t, size, color):
    """
    draw a diamond
    :param t: turtle object
    :param size: integer
    :param color: pen color
    :return: None
    """
    t.pd()
    t.color(color)
    t.fd(size)
    t.rt(20)
    t.fd(size)
    t.rt(160)
    t.fd(size)
    t.rt(20)
    t.fd(size)
    t.pu()


def drop(t, size, color):
    """
    draw a drop
    :param t: turtle object
    :param size: integer
    :param color: pen color
    :return: none
    """
    t.pd()
    t.color(color)
    t.fd(size)
    t.circle(size / math.sqrt(3), 240)
    t.fd(size)
    t.rt(size)
    t.pu()


if __name__ == '__main__':
    main()
