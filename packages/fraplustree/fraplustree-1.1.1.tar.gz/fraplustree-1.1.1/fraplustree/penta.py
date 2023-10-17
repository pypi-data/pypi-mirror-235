import turtle
import math

def star(x,y,direction,r): #x,y is the center
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(direction)
    turtle.fd(r)
    turtle.right(180-18)
    turtle.down()
    length = 2*r*math.sin(math.pi*2/5)
    for _ in range(5):
        turtle.fd(length)
        turtle.right(180-36)

def star_fractal(x,y,direction,r, max_r):
    star(x,y,direction,r)
    if r < max_r: return
    star_fractal(x,y,180+direction,r*math.sin(math.pi/10)/math.cos(math.pi/5), max_r)
    turtle.done()


def generate_penta(max_r=20):
    screen = turtle.Screen()
    screen.title('Pentagram Fractal - PythonTurtle.Academy')
    screen.setup(1000, 1000)
    screen.setworldcoordinates(-1000, -1000, 1000, 1000)
    turtle.speed(0)
    turtle.hideturtle()
    star_fractal(0,0,90,1000, max_r)
