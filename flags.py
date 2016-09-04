#! /usr/local/bin/python

from colored import bg, attr
import countries
import sys
import inspect
import argparse

# Flag width/height, in chars
width = 30
height = 9

# Default symbol to use to draw
symbol = " "

# Colours
orange           = bg('orange_3')
green            = bg('dark_green')
white            = bg('white')
red              = bg('red')
blue             = bg('blue')
navy_blue        = bg('navy_blue')
yellow           = bg('yellow')
light_yellow     = bg('light_yellow')
black            = bg('black')
light_green      = bg('light_green')
res              = attr('reset')

def verticalTricolour(left, middle, right):
    flag = ''
    for row in xrange(0,height):
        for column in xrange(0,width):
            if (column < width/3):
                flag += left + symbol + res
            elif (column < 2*width/3):
                flag += middle + symbol + res
            else :
                flag += right + symbol + res
        flag += ('\n')
    return flag

def verticalTricolourWideCentre(left, middle, right):
    flag = ''
    for row in xrange(0,height):
        for column in xrange(0,width):
            if (column < width/3 - width/30):
                flag += left + symbol + res
            elif (column < 2*width/3 + width/30):
                flag += middle + symbol + res
            else :
                flag += right + symbol + res
        flag += ('\n')
    return flag

def horizontalTricolour(top, middle, bottom):
    flag = ''
    for row in xrange(0,height):
        for column in xrange(0,width):
            if (row < height/3):
                flag += top + symbol + res
            elif (row < 2*height/3):
                flag += middle + symbol + res
            else :
                flag += bottom + symbol + res
        flag += ('\n')
    return flag

def horizontalTricolourWideCentre(top, middle, bottom):
    flag = ''
    for row in xrange(0,height):
        for column in xrange(0,width):
            if (row < height/3 - height/9):
                flag += top + symbol + res
            elif (row < 2*height/3 + height/9):
                flag += middle + symbol + res
            else :
                flag += bottom + symbol + res
        flag += ('\n')
    return flag

def horizontalTricolourWideTop(top, middle, bottom):
    flag = ''
    localHeight = height - (height%4)
    localWidth = width
    for row in xrange(0,localHeight):
        for column in xrange(0,width):
            if (row < height/2):
                flag += top + symbol + res
            elif (row < 3*height/4):
                flag += middle + symbol + res
            else :
                flag += bottom + symbol + res
        flag += ('\n')
    return flag

def scandinavianCross(background,innerCross, outerCross):
    flag = ''
    for row in xrange(0,height):
        for column in xrange(0,width):
            if (height/2 - width/30 + 1 <= row <= height/2 + width/30 - 1  or 4*width/15 - width/30 <= column <= 4*width/15 + width/30):
                flag += innerCross + symbol + res
            elif (height/2 - width/30 <=  row <= height/2 + width/30 or 4*width/15 - width/10 <= column <=  4*width/15 + width/10):
                flag += outerCross + symbol + res
            else:
                flag += background + symbol + res
        flag += ('\n')
    return flag

def horizontalBicolour(top, bottom):
    flag = ''
    localHeight = height - (height%2)
    localWidth = width
    for row in xrange(0,localHeight):
        for column in xrange(0,width):
            if (row < height/2):
                flag += top + symbol + res
            else:
                flag += bottom + symbol + res
        flag += ('\n')
    return flag

def verticalBicolour(left,right):
    flag = ''
    localHeight = height
    localWidth = width - (width%2)
    for row in xrange(0,localHeight):
        for column in xrange(0,localWidth):
            if (column < localWidth/2):
                flag += left + symbol + res
            else:
                flag += right + symbol + res
        flag += ('\n')
    return flag

def main():
    parser = argparse.ArgumentParser(description='Print flags in ASCII')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c','--country', help='Country to show')
    group.add_argument('-a', '--all', action='store_true', help='Print all available flags')
    args = vars(parser.parse_args())

    if (args['all']):
        name_func_tuples = inspect.getmembers(countries, inspect.isfunction)
        name_func_tuples = [t for t in name_func_tuples if inspect.getmodule(t[1]) == countries]
        functions = dict(name_func_tuples)
        for function_name in functions:
            print(functions[function_name]())
    elif(args['country']):
        printFunction = hasattr(countries, args['country'].lower())
        if(hasattr(countries, args['country'].lower())):
            print(getattr(countries, args['country'].lower())()),
        else:
            print ('Flag not implemented')


if __name__ == "__main__":
    main()
