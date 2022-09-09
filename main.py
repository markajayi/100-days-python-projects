# nepa = input("Is NEPA on? type 'ON' or 'OFF': ")
# gen = input("Is GEN on? type 'ON' or 'OFF': ")
# nepa1 = nepa.upper()
# gen1 = gen.upper()
#
# if nepa1 == "OFF" and gen1 == "OFF":
#     print("Switch to NEPA supply")
# elif nepa1 == "OFF" and gen1 == "ON":
#     print("Switch to GEN supply")
# elif nepa1 == "ON" and gen1 == "OFF":
#     print("Switch to NEPA supply")
# elif nepa1 == "ON" and gen1 == "ON":
#     print("Switch to NEPA supply")
# else:
#     print("Invalid input. Check your input")
# numbers =[]
# for num in range(0, 100):
#     square = num * num
#     numbers.append(square)
# print(square)
# Write a programme that reverses the digits of a given number
# number = input("Enter a number: ")
# reverse = 0
# while number > 0:
#     reminder = number % 10
#     reverse = (reverse * 10) + reminder
#     number = number // 10
# print("\n reverse of entered number is =%d" % reverse)


# string = list(number)
# print(string)
# string.reverse()
# string = ''.join(string)
# num = int(string)
# print(num)

# using slicing method to reverse a given number1
# number = [2, 3, 4, 4, 5, 6, 7, 7, 8, 8]
#
# num = number[:: -1]
# print(num)

# Using the turtle module to draw a square
import random

import turtle as t

tim = t.Turtle()
t.colormode(255)


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


#
#
# angle = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.setheading(random.choice(angle))
#     tim.color(random_color())
#     tim.forward(30)

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()
