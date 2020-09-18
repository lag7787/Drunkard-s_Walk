#Luc Garabrant 6/4/2019
#
#This Program Will Simulate a Drunkard's Walk

import turtle
import time
import random

def grid(lines, window):

    width = window.window_width()
    height = window.window_height()

    halfW = width // 2
    halfH = height // 2
    
    
    lines.speed(0)
        
    for x in range(-halfW,halfW,10):
    
        lines.penup()
        lines.setposition(x,halfH)
        lines.pendown()
        lines.setposition(x,-halfH)
        
    for x in range(-halfH,halfH,10):
        
        lines.penup()
        lines.setposition(halfW,x)
        lines.pendown()
        lines.setposition(-halfW,x)
        
def walk(ourTurtle,ourSpeed):
    
    ourTurtle.pensize(2)
    ourTurtle.color('Red')
    ourTurtle.speed(ourSpeed)
    direction = random.randint(1,4)
    pos = ourTurtle.position()
    
    if direction % 2 == 0:

        if direction == 2:
            ourTurtle.setposition(pos[0],int(pos[1]+10))
            
        else:
           ourTurtle.setposition(pos[0],(int(pos[1]-10)))
    else:
        if direction == 1:
            ourTurtle.setposition(int(pos[0]) + 10, pos[1])
        else:
            ourTurtle.setposition((int(pos[0]) - 10), pos[1])
           

def main():

    turtle.setup(800,800)
    window = turtle.Screen()
    window.title('A Drunkard\'s Walk') 
    lines = turtle.Turtle()
    drunkTom = turtle.Turtle()
    
    print('This program will simulate a random Drunkard\'s Walk\n')
    howLong = input('Enter number of seconds to run: ')
    while not howLong.isdigit() or int(howLong) <= 0:
        howLong = input('Invalid Input. Enter number of seconds to run: ')
    howFast = input('Enter speed (1-slow,2-faster,... 10-fastest): ')
    while not howFast.isdigit() or (int(howFast) < 1 or int(howFast) > 10):
         howFast = input('Invalid Input.Enter speed (1-slow,2-faster,... 10-fastest): ')
    howFast = int(howFast)
    grid(lines, window)
    startTime = time.time()
    while (time.time() - startTime) < int(howLong) :
        walk(drunkTom,howFast)
    
main()
