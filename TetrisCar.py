#Team Members:
#--Ruben A.
#--Cesar Neri        
#March 16, 2017
#CMPS 5P Final Project

#TetrisCar.py

#Object of type TetrisCar defines the game platform. Object of type TetrisCar defines
#list of Obstacle objects as well as a single Car object. It defines method to
#mantainb the game and its elements.

#Main funtion: Creates object of type TetrisCar. Inside a loop, it updates the state of each obstacle, and using a keyboard listener
#of TetrisCar. Also uses Keyboard listener


#!/usr/bin/env python

#Python pre-defined modules
import pygame, sys, time
import random as rd
from pygame.locals import *

#Custom modules
import ADTs as adt
import Car as cr
import Obstacle

class TetrisCar:

    #Constructor takes single parameter "speed"
    def __init__(self, speed = .014):
        self.__score = 0
        self.__speed = speed
        
        #Lnked List stores a list of Obstacle objects
        self.__obstacles = adt.LinkedList()
        #Create single object of type car
        self.__auto = cr.Car()

    #Score getter
    @property
    def score(self):
        return self.__score

    #Speed getter
    @property
    def speed(self):
        return self.__speed

    #Score increment
    def score_up(self):
        self.__score += 10

    #Moves car right
    def move_right(self):
        self.__auto.moveRight()

    #Moves car left
    def move_left(self):
        self.__auto.moveLeft()

    #Adds an empty spot to the list of Obstacles (10 represents "empty")
    def add_space(self):
        self.__obstacles.append(10)

    #Adds object of type Obstacle to the list of Obstacles
    def add_obstacle(self):

        #Define 3 possible lane coordinate choices
        lane = ( (160,10), (223,10), (286,10) )
        
        #Define 3 random RGB values 
        r = rd.randint(0,255)
        g = rd.randint(0,255)
        b = rd.randint(0,255)

        #Create a color Tuple
        color = (r, g, b)
        
        #Random lane
        l = rd.randint(0, 2)
        
        #Create new obstacle
        new_obstacle = Obstacle.Obstacle(l, color, lane[l])

        #Add obstacle to the end of the list
        self.__obstacles.append(new_obstacle)

    #Initializes the list of obstacles to filled only with empty spaces initially
    def start(self):

        for i in range(40):
            self.add_space()

    #Advances every obstacle forward
    def road_fwd(self):

        #For every obstacle object in list of obstacles call its advance() method
        for o in self.__obstacles:
            if type(o) is Obstacle.Obstacle:
                o.advance()

        #Delete the element at the fron of the list
        #(Element has gone out of window scope)
        self.__obstacles.removeHead()

        #Every 12 iterations add a new obstacle
        if self.score % 120 == 0:
            self.add_obstacle()
        #Otherwise add a space (Spaces in between vehicles)
        else:
            self.add_space()

        #Increment the score
        self.score_up()

    #Returns true if a part of an obstacle's body collides with car object 
    def check_collision(self):

        count = 0
            
        #We go trough the obstacle objects in the Obstacle list
        for o in self.__obstacles:

            #We only check the first 10 elements in the list, the remaining are
            #too far from our car and it is not necessary to check them
            if count > 10:
                break

            #Check if it is an Obstaclke object 
            if type(o) is Obstacle.Obstacle:
                #Check if y coordinates are within those of the Car object
                #and if the lane is the same return True
                if o.y > 310 and o.y < 490 and o.lane == self.__auto.lane:
                    return True
                
            #Increment Count    
            count += 1

        return False          

    #Draw backgroud image (The road) in specified display
    def draw_background(self, Display):
        
        #Define colors needed
        White = (255,255,255)
        Gray = (50,50,50)
        Green = (0,255,0)

        #Fill the back just in case
        Display.fill(White)

        #Draw Road 
        pygame.draw.rect(Display,Gray,(150,0,189,400))
        #Draw Lanes
        pygame.draw.rect(Display,White,(211,0,5,400))
        pygame.draw.rect(Display,White,(274,0,5,400))

        #Draw Grass
        pygame.draw.rect(Display,Green,(0,0,150,400))
        pygame.draw.rect(Display,Green,(339,0,150,400))

        #Define font, size and set to bold
        myfont = pygame.font.SysFont("monospace", 14)
        myfont.set_bold(True)

        #Render text in label
        label = myfont.render("Use LEFT and", 1, (0,0,0))
        Display.blit(label, (5, 20))
        label = myfont.render("RIGHT arrows", 1, (0,0,0))
        Display.blit(label, (5, 35))
        label = myfont.render("to avois the", 1, (0,0,0))
        Display.blit(label, (5, 50))
        label = myfont.render("other vehicles!", 1, (0,0,0))
        Display.blit(label, (5, 65))
        
    #Draw game screen in specified display
    def draw_screen(self, Display):

        #Draw background
        self.draw_background(Display)

        #Go trough the list of obstacles, and draw every object of type Obstacle
        for o in self.__obstacles:
            if type(o) is Obstacle.Obstacle:
                o.draw(Display)

        #Draw the Car object
        self.__auto.draw(Display)

    #End game and draw Game Over screen
    def game_over(self, Display):

        #Cover screen with black rectangle
        pygame.draw.rect(Display,(0,0,0),(0,0,480,400))

        #Define font, size and set to bold
        myfont = pygame.font.SysFont("monospace", 30)
        myfont.set_bold(True)

        #Render text in label
        label = myfont.render("Game Over", 1, (255,0,0))
        Display.blit(label, (150, 200))

        #Update screen
        pygame.display.update()

        #Delay
        time.sleep(2)

        #Close window
        pygame.quit()
        sys.exit()


#-----------------------MAIN------------------------------
def main():    

    #Initialize Pygame modules 
    pygame.init()

    #Define and set dispolay window
    Display = pygame.display.set_mode((480,400),0,32)

    #Change caption
    pygame.display.set_caption('The Speedy and the Infuriated!')

    #Define and initialize Tetriscar object
    game = TetrisCar()
    game.start()

    #Draw screen initially
    game.draw_screen(Display)
            
    #Update screen
    pygame.display.update()

    #Delay, to make instructions visible game visible
    time.sleep(1)

    #Game Loop
    while True:  

        #Listen to events
        for event in pygame.event.get():

            #User closes window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Keiy is pressed
            pressed = pygame.key.get_pressed()
            #Right arrow pressed
            if pressed[pygame.K_RIGHT]:
                game.move_right()
            #Left arrow pressed
            if pressed[pygame.K_LEFT]:
                game.move_left()

        #Advance every element (1 iteration of the game)
        game.road_fwd()

        #Check if there is a collision
        if game.check_collision():
            #If so end the game
            game.game_over(Display)

        #Redraw screen
        game.draw_screen(Display)
            
        #Update screen
        pygame.display.update()
        
        #Delay, to make game visible
        time.sleep(game.speed)


if __name__ == "__main__":
    main()

    

        
