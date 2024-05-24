#Anoushka Saha
#Snake Game
#Day 21 & 22 Project
#May 19th, 2024

from turtle import Turtle, Screen

#Creating screen object
screen = Screen()

#Screen dimensions
screen.setup(width=600, height=600)

#Screen background colour
screen.bgcolor("black")

#Display title
screen.title("Snake Game")

#Create snake object
snake = Turtle()
snake.shape("square")
snake.color("white")

screen.exitonclick()