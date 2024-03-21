# File Name: HW2_112652050.py
# Author: Yu-Hsiang, Wang
# Email Address: yh.sc12@nycu.edu.tw
# HW Number: 2
# Description: Using different ways to estimate pi.
# Last Changed: Mar. 10, 2024
# Anything special?
# (1) I added error percentages and using decimal.Decimal to calculate
# (2) I used a lot of f-string to make the output look good
# (3) In part I, I showed the result of how many points that
#                inside/outside the quarter circle
#                If sample points >= 100 I let tracer(0, 0).
#                There will be a prompt after completion.
# (4) I added part III, estimating Pi by viete's formula


# I used python 3.21.2 (which has turtle.teleport)

# technical supports
# 112652044: decimal


# import modules
import turtle
import random

from math import pi, sqrt
from decimal import Decimal, getcontext

# declaration of constants
SET_TEXT_GREEN = '\n\033[32m'
SET_TEXT_WHITE = '\033[0m'

SCREEN_SIZE = 400
PI = Decimal(pi)

# set precision to 60 digits
getcontext().prec = 60


def show_monte_carlo_pi(samplePoints):
    # set up canvas
    screen = turtle.Screen()
    screen.screensize(SCREEN_SIZE, SCREEN_SIZE)

    # set up coordinates
    screen.setworldcoordinates(0, 0, 1, 1)

    # set up turtle
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed('fastest')

    if samplePoints >= 100:
        turtle.tracer(0, 0)

    # draw the quarter
    pen.teleport(1, 0)
    pen.setheading(90)
    pen.circle(1, 90, 30)

    inCircle = 0  # number of points in the circle

    for _ in range(samplePoints):
        x = random.random()
        y = random.random()
        distance = sqrt(x ** 2 + y ** 2)

        if distance <= 1:
            inCircle = inCircle + 1
            pen.color("Blue")
        else:
            pen.color("Red")

        pen.teleport(x, y)
        pen.dot()  # draw a blue or red dot at (x, y)

    # calculate pi
    estimatedPi = Decimal(inCircle / samplePoints * 4)

    # show info
    pen.color('Orange')
    pen.teleport(0.5, 0.5)
    pen.write('FINISHED',
              align='center', font=('Arial', 45, 'normal'))

    pen.color('Green')
    pen.teleport(0.5, 0.45)
    pen.write('Click To Continue',
              align='center', font=('Arial', 27, 'normal'))

    # print the result
    print(f'There are {inCircle} points inside the quarter '
          f'and {samplePoints - inCircle} points outside the quarter.')

    # screen exit on click
    screen.exitonclick()

    return estimatedPi


def leibniz_formula(terms):
    acc = Decimal(0)  # accumulator
    num = Decimal(4)  # numerator
    den = Decimal(1)  # denominator

    for term in range(terms):
        nextTerm = num / den * (-1) ** term
        acc += nextTerm  # adding next term
        den += 2  # increase denominator by 2

    return acc


def nilakantha_formula(terms):
    acc = Decimal(3)  # accumulator
    num = Decimal(4)  # numerator
    den = Decimal(3)  # denominator

    for term in range(1, terms):
        next_term = num / (den ** 3 - den) * (-1) ** (term - 1)
        acc += next_term  # adding next term
        den += 2  # increase denominator by 2

    return acc


def viete_formula(terms):
    acc = Decimal(sqrt(2) / 2)  # accumulator
    num = Decimal(sqrt(2))  # numerator
    den = Decimal(2)  # denominator

    for term in range(terms):
        num = Decimal(sqrt(2 + num))  # increase numerator
        acc *= num / den  # multiplies acc

    return 2 / acc


def part_I():
    print(SET_TEXT_GREEN + 'Part I' + SET_TEXT_WHITE +
          ' (using Monte Carlo method to estimate pi) ')

    num = int(input('Please enter the number of sample points. '))
    print(f'Echo the number you entered: {num:,}\n')

    estimatedPi = show_monte_carlo_pi(num)
    estimatedPiError = Decimal((estimatedPi - PI) / PI)

    print(f'The value of pi by Monte Carlo method for {num:,} numbers is '
          f'{estimatedPi} (error: {estimatedPiError:+.2%})')


def part_II():
    print(SET_TEXT_GREEN + 'Part II' + SET_TEXT_WHITE +
          ' (using Leibniz Formula and Nilakantha Formula to estimate pi) ')

    # heading
    print(f'{'Terms':^5}'
          f'{'Leibniz Formula':^52} {f'(error)':12}'
          f'{'Nilakantha Formula':^52} {f'(error)':12}')

    # divider
    for _ in range(135):
        print('=', end='')
    print()

    # num = 1 ~ 9
    for num in range(1, 10):
        leibnizValue = leibniz_formula(num)
        nilakanthaValue = nilakantha_formula(num)

        leibnizError = Decimal((leibnizValue - PI) / PI)
        nilakanthaError = Decimal((nilakanthaValue - PI) / PI)

        print(f'{num:<5}'
              f'{leibnizValue:.50f} '
              f'{f'({leibnizError:+.2%})':12}'
              f'{nilakanthaValue:.50f} '
              f'{f'({nilakanthaError:+.2%})':12}')

    # num = 10^1 ~ 10^7
    for power in range(1, 8):
        leibnizValue = leibniz_formula(10 ** power)
        nilakanthaValue = nilakantha_formula(10 ** power)

        leibnizError = Decimal((leibnizValue - PI) / PI)
        nilakanthaError = Decimal((nilakanthaValue - PI) / PI)

        print(f'{10}^{power:<2}'
              f'{leibnizValue:.50f} '
              f'{f'({leibnizError:+.2E})':12}'
              f'{nilakanthaValue:.50f} '
              f'{f'({nilakanthaError:+.2E})':12}')


def part_III():
    print(SET_TEXT_GREEN + 'Part III' + SET_TEXT_WHITE +
          ' (using viete\'s formula method to estimate pi) ')

    num = int(input('Please enter the number of terms to estimate pi. '))
    print(f'Echo the number you entered: {num:,}\n')

    vieteValue = viete_formula(num)
    vieteValueError = Decimal((vieteValue - PI) / PI)

    print(f'The value of pi by finite product method for {num:,} numbers is\n'
          f'{vieteValue:.50f} (error: {vieteValueError:+.2E})')


def main():
    part_I()
    part_II()
    part_III()


if __name__ == "__main__":
    main()
