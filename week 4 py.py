
import turtle
import math
import random

def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def square(t, length):
    rectangle(t, length, length)

def rectangle(t: turtle.Turtle, base, height):
    for length in (base, height, base, height):
        t.forward(length)
        t.left(90)

def draw_circle(t: turtle.Turtle, radius):
    t.circle(radius)

def draw_polygon(t: turtle.Turtle, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

""" Fun Present demo
def polyline(t: turtle.Turtle,n ,length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t: turtle.Turtle, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t, n, length, step_angle)
def draw_ribbon(t: turtle.Turtle, x, y, base, height, color="green"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base, height)
    t.end_fill()

def draw_bow(t: turtle.Turtle, x, y, bow_size):
    jump(t,x ,y)
    t.color("green")
    t.pensize(5)
    t.right(15)
    arc(t, bow_size, 120)
    t.left(60)
    arc(t, bow_size, 120)
    t.right(195)
    arc(t, bow_size, 120)
    t.left(60)
    arc(t, bow_size, 120)
    t.color("white")

def draw_present(t:turtle.Turtle, x, y, base, height, ribbon_width, color="red"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t,base,height)
    t.end_fill()
    p_center = (x + (base / 2))
    r_x = (p_center) - (ribbon_width /2)
    draw_ribbon(t, r_x, y, ribbon_width, height)
    r_y = (y + (height / 2)) - (ribbon_width / 2)
    draw_ribbon(t, x , r_y, base, ribbon_width)
    draw_bow(t, p_center, y + height, base/3)
    
    # draw_present(t, 1,1, 69,69,5)
"""


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    jump(t, x+(radius //10), y + (radius) * 2)
    # Drawing the stem
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_eye(t, x, y, size):
        """Draws one triangular eye at the given (x, y) position."""
        jump(t, x, y)
        t.fillcolor("yellow")
        t.begin_fill()
        draw_polygon(t, 3, size)
        t.end_fill()

def draw_mouth(t, x, y, width):
        """Draws a jagged mouth using a series of connected lines."""
        jump(t, x, y)
        t.fillcolor("yellow")
        t.begin_fill()
        t.right(60)
        for _ in range(5):  # Create a simple zigzag mouth
            t.forward(width // 5)
            t.left(120)
            t.forward(width // 5)
            t.right(120)
        t.end_fill()
        t.left(60)
def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_jack(t,x,y,radius):
    draw_pumpkin(t, x, y, radius)  # Draw the pumpkin
    eye_height = y+.55*2*radius
    mouth_height = y + .3*2*radius
    draw_eye(t, x - .333*radius, eye_height, radius/3.5)  # Left eye
    draw_eye(t, x + .333*radius, eye_height, radius/3.5)   # Right eye
    draw_mouth(t, x - .333* radius, mouth_height, radius)  # Mouth


# create a turtle object

t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()
# draw_sky(t, 20)  # Draw 20 stars
# draw_pumpkin(t, 0, -100, 100)  # Draw the pumpkin
# draw_eye(t, -40, 0, 30)  # Left eye
# draw_eye(t, 40, 0, 30)   # Right eye
# draw_mouth(t, -50, -50, 100)  # Mouth

draw_sky(t, 20)  # Draw 20 stars
draw_jack(t,-150,-250, 100)
draw_jack(t,150,-250, 75)
draw_jack(t,0,-250, 50)


# Close the turtle graphics window when clicked
turtle.exitonclick()










