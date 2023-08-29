from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def create_turtle(colour, position):
    # Create turtle and place it in the start position
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(x=-230, y=position)
    return new_turtle


pos = -100
turtles = []
# create a turtle for every color
for color in colors:
    turtle = create_turtle(color, pos)
    turtles.append(turtle)
    pos += 50

if user_bet:
    is_race_on = True

while is_race_on:
    # move forward every turtle by a random number
    for turtle in turtles:
        if turtle.xcor() > 230:  # check to determine if the current turtle has reached the goal line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
