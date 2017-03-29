#Team Members:
#--Ruben A.
#--Cesar Neri
#March 16, 2017
#CMPS 5P Final Project

#Obstacle.py

#Object of type Obstacle specifies its current lane, color, and coordinates. All
#three values are permanent and cannot be changed

import pygame, sys
from pygame.locals import *

import random as rd


class Obstacle:

    #Constructor
    def __init__(self, lane, color, coord):
        
        #Data validation
        if lane < 0 or lane > 2:
            raise ValueError()

        if len(coord) != 2:
            raise ValueError()
        
        if len(color) != 3:
            raise ValueError()
        
        #Set permanent values 
        self.__lane = lane
        self.__x = coord[0]
        self.__y = coord[1]
        self.__color = color

    #Lane getter
    @property
    def lane(self):
        return self.__lane

    #x coordinate getter
    @property
    def x(self):
        return self.__x

    #y coordinate getter
    @property
    def y(self):
        return self.__y

    #Color getter
    @property
    def color(self):
        return self.__color

    #Object moves forward in the screen (By 10 pixels)
    def advance(self):
        self.__y += 10


    #Obstacle object draws itself in the spcified window
    def draw(self, Display):
        #Get current coordinates
        x = self.x
        y = self.y

        #Define colors needed
        color = self.color
        Black = (0,0,0)
        White = (255,255,255)

        #Draw the "Chasis"
        pygame.draw.rect(Display,color,(x + 12, y, 20, 40))

        #Top left suspension
        pygame.draw.rect(Display,color,(x+8,y+10,10,5))
        #Bottom left suspension
        pygame.draw.rect(Display,color,(x+8,y+30,10,5))
        #Top right suspension
        pygame.draw.rect(Display,color,(x+28,y+10,10,5))
        #Bottom right suspension
        pygame.draw.rect(Display,color,(x+28,y+30,10,5))

        #Top left wheel
        pygame.draw.rect(Display,Black,(x,y+5,8,15))
        #Bottom left wheel
        pygame.draw.rect(Display,Black,(x,y+25,8,15))
        #Top right wheel
        pygame.draw.rect(Display,Black,(x+35,y+5,8,15))
        #Bottom right wheel
        pygame.draw.rect(Display,Black,(x+35,y+25,8,15))

        #Window
        pygame.draw.rect(Display,White,(x+17,y + 20,10,10))

        
        
