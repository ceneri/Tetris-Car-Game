#Team Members:
#--Ruben A.
#--Cesar Neri           
#March 16, 2017
#CMPS 5P Final Project

#Car.py

#Object of type Car specifies its current lane, and its corresponding
#coordinates on the window


#!/usr/bin/env python


import pygame
from pygame.locals import *

import random as rd

class Car:

    #Constructor
    def __init__ (self):
        #By default car is initialized in the middle lane
        self.__lane = 1
        self.__x = 223
        self.__y = 350

    #Lane getter
    @property
    def lane(self):
        return self.__lane

    #Lane setter
    @lane.setter
    def lane(self, lane):
        self.__lane = lane
    
    #Changes to right lane if necessary
    def moveRight(self):
        #1st or 2nd lane --->  2nd lane
        if self.lane == 1 or self.lane == 2:
            self.lane = 2
            self.__x = 286
        #0 lane --->  1st lane
        elif self.lane == 0:
            self.lane = 1
            self.__x = 223
            
    #Changes to left lane if necessary
    def moveLeft(self):
        #1st or 0 lane --->  0 lane
        if self.__lane == 1 or self.__lane == 0:
            self.__lane = 0
            self.__x = 160
        #2nd lane --->  1st lane
        elif self.__lane == 2:
            self.__lane = 1
            self.__x = 223

    #Car object draws itself in the spcified window
    def draw(self, Display):
        #Get current coordinates
        x = self.__x
        y = self.__y

        #Define colors needed
        Red = (255,0,0)
        Black = (0,0,0)
        White = (255,255,255)

        #Draw the "Chasis"
        pygame.draw.rect(Display,Red,(x + 12, y, 20, 40))

        #Top left suspension
        pygame.draw.rect(Display,Red,(x+8,y+10,10,5))
        #Bottom left suspension
        pygame.draw.rect(Display,Red,(x+8,y+30,10,5))
        #Top right suspension
        pygame.draw.rect(Display,Red,(x+28,y+10,10,5))
        #Bottom right suspension
        pygame.draw.rect(Display,Red,(x+28,y+30,10,5))

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






    
