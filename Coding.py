import turtle as tur
import random

tur.speed(5)
tur.tracer(2)
tur.setup(500, 600)
tur.bgcolor('black')
tur.title("starry night")

# Function to draw stars
def draw_star(x, y, size, color):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()
    tur.color(color)
    tur.begin_fill()
    for _ in range(5):
        tur.forward(size)
        tur.right(144)
    tur.end_fill()
    
#Draw numbers randomly
num_stars = 100
colors = ['white', 'yellow', 'cyan', 'orange', 'lightgreen', 'lightblue']

for _ in range(num_stars):
    x = random.randint(-250, 250)
    y = random.randint(-300, 300)
    size = random.randint(5, 20)
    color = random.choice(colors)
    draw_star(x, y, size, color)

#hide the tur cursor
    tur.hideturtle

# keep the window open until closed manually
    tur.done()