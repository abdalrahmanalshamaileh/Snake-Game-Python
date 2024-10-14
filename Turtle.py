import turtle as t
from turtle import Screen, Turtle
from random import randint, choice
import time
from newsnake import Snake  # Ensure this file is correct
from food import Food       # Ensure this file is correct
from scoreboard import Score # Ensure this file is correct

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off automatic updates to allow for smooth animations

# Create instances of the Snake, Food, and Scoreboard
s = Snake()  # Snake object from your external file
f = Food()   # Food object from your external file
score = Score()  # Scoreboard object from your external file

# Set up keybindings to control the snake
screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_is_on = True

# Main game loop
while game_is_on:
    screen.update()
    time.sleep(0.05)  # Control the game speed
    s.move()  # Move the snake

    # Detect collision with food
    if s.head.distance(f) < 15:
        f.refresh()  # Reposition the food
        s.extend()   # Extend the snake body
        score.increase_score()  # Update the score

    # Detect collision with wall
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail (ignore the first segment which is the head)
    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            game_is_on = True
            # score.game_over()

# Close the window when clicked
screen.exitonclick()
