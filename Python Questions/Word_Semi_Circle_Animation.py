# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:38:30 2020

@author: Akuto Sai
"""

import turtle
# import random
from alphabet import alphabet
# from math import cos, sin, radians
from math import atan2,  degrees 

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y,rotationAngle):
  myPen.color(color)
  message=message.upper()
  myPen.penup()
  myPen.goto(x,y)  
  for Char in message:
    if Char in alphabet:
      letter=alphabet[Char]
      myPen.setheading(rotationAngle)
      myPen.penup()
    
      x=0
      y=0
      for dot in letter:
        angle = atan2((dot[1]-y),(dot[0]-x))
        angle= degrees(angle)    
  
        distance = ((dot[0]-x)**2 + (dot[1]-y)**2)**0.5
        myPen.setheading(rotationAngle)
  
        myPen.left(angle)
        myPen.forward(distance*fontSize)
        x = dot[0]
        y = dot[1]
        myPen.pendown()
  
      myPen.penup()
      angle = atan2((0-y),(0-x))
      angle = degrees(angle)    
  
      distance = ((0-x)**2 + (0-y)**2)**0.5
      myPen.setheading(rotationAngle)
  
      myPen.left(angle)
      myPen.forward(distance*fontSize)
  
    myPen.setheading(rotationAngle)
    myPen.penup()
    myPen.forward(fontSize)    
    
    myPen.forward(CharSpacing)
    

#Main Program 
    
fontSize = 30
fontColor="#00FF15"
CharSpacing = 5
cursorX = -150
cursorY = -100

message = "DANCE DUDE"
rotationAngle=90
myPen.goto(cursorX,cursorY)

for Char in message:
  pos=myPen.position()
  displayMessage(Char,fontSize,fontColor,pos[0],pos[1],rotationAngle)
  rotationAngle-=180/(len(message)-1)