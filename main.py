from turtle import Turtle, Screen
import turtle as t
import random


turtle = Turtle()
screen = Screen()

t.colormode(255)

turtle.penup()
turtle.hideturtle()
color_list = (244, 245, 75), (164, 2, 52), (11, 28, 75), (23, 95, 166), (170, 76, 15), (191, 167, 14), (75, 0, 19), (208, 247, 247), (99, 234, 217), (196, 98, 127), (243, 226, 234), (3, 56, 132), (82, 190, 216), (41, 12, 3), (223, 214, 6), (93, 81, 15), (22, 201, 209), (88, 227, 100), (14, 82, 88), (216, 175, 65), (204, 122, 149), (83, 92, 181), (171, 53, 81), (27, 204, 199), (169, 22, 3), (198, 224, 239), (192, 89, 76), (224, 170, 195), (20, 86, 83), (122, 220, 230), (14, 69, 67), (175, 184, 221), (58, 109, 105), (220, 178, 170)

turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)
turtle.speed(30)
num_of_dots = 100

for i in range(1, num_of_dots + 1):

    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)








screen.exitonclick()