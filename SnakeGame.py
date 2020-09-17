from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


# Random Snake and Food color Generators __________________________________________

colors_list = ["green","yellow","blue","black","pink","purple", "orange"]
snake_color = colors_list[random.randint(0,len(colors_list)-1)]
food_color = colors_list[random.randint(0,len(colors_list)-1)]

while snake_color==food_color:
    food_color = colors_list[random.randint(0,len(colors_list)-1)]



# Change snake direction __________________________________________

def change(x, y):
    aim.x = x
    aim.y = y



# Boundaries Checker __________________________________________

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


# Snake & Food Movement __________________________________________

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    food.x = randrange(-5, 5) * 10
    food.y = randrange(-5, 5) * 10
    # Makes the food move around as you move
    if(-200 >food.x >190 or -200 > head.y > 190 ):
        food.x = 10
        food.y = 10
    update()
    ontimer(move, 100)


# Program Init __________________________________________

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
