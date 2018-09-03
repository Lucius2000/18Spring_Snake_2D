# This is the latest version of the Snake Game.

from tkinter import *
from tkinter import font
import pygame
import random

# Here is the basic structure about Snake and Food
class Snake:

    def __init__(self,blocksize):
        self.blocksize = blocksize
        self.pos = [[0,1],[1,1],[2,1],[3,1]]
        A = ["Right","Left","Up","Down"]
        self.dir= A[random.randint(0,3)]


    def changeDirection(self,dir):
        if dir == "Right" and self.dir != "Left":
            self.dir = dir
        if dir == "Left" and self.dir != "Right":
            self.dir = dir
        if dir == "Up" and self.dir != "Down":
            self.dir = dir
        if dir == "Down" and self.dir != "Up":
            self.dir = dir

    def move(self):
        (x,y) = self.pos[-1]
        if self.dir == "Up":
            self.pos.append([x, y - 1])
        if self.dir == "Down":
            self.pos.append([x, y + 1])
        if self.dir == "Left":
            self.pos.append([x-1,y])
        if self.dir == "Right":
            self.pos.append([x + 1, y])
        del self.pos[0]


    def grow(self):
        (x, y) = self.pos[-1]
        if self.dir == "Right":
            self.pos.append([x + 1, y])
        if self.dir == "Left":
            self.pos.append([x - 1, y])
        if self.dir == "Up":
            self.pos.append([x, y - 1])
        if self.dir == "Down":
            self.pos.append([x, y + 1])



    def update(self):
        self.move()
        pass
		
    def render(self,canvas):
        for (x,y) in self.pos:
            canvas.create_rectangle(
                x * self.blocksize,
                y * self.blocksize,
                (x+1) * self.blocksize,
                (y+1)* self.blocksize,
                 fill = "#3875EE"
            )

class Food:
    def __init__(self, width, height,blocksize):
        # Randomly generate the food
        self.blocksize= blocksize
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        pass
	
    def update(self):
        # Probably do nothing here.
		# I added this function just to follow this design pattern.
        pass
	
    def render(self,canvas):
        canvas.create_rectangle(
            self.x * self.blocksize,
            self.y * self.blocksize,
            (self.x + 1) * self.blocksize,
            (self.y + 1) * self.blocksize,
            fill = "#EE8838"
        )

class State:
    Running = 0
    Menu = 1
    Gameover = 2

class Launcher:

    def __init__(self, width, height):
        self.frame = Tk()
        self.frame.title('Snake Game By Luo')
        self.width = width
        self.height = height
        self.blocksize=20
        self.canvas = Canvas(self.frame, width = self.width * self.blocksize, height = self.height * self.blocksize, bg = "#F7FBFE")
        self.canvas.pack()
        self.frame.bind("<Key>", self.keyboardInput)
        # Here are all the properties about game objects
        self.snake=Snake (self.blocksize)
        self.food= Food(self.width, self.height,self.blocksize)
        self.score = 0
        # Soundsystem
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Sound("bite.wav")
        #a command to turn on the sound player lol
        
        self.overSound = pygame.mixer.Sound ("die.wav")
        # could add a lot more sound



    # These is the Event functions
    def keyboardInput(self, event):
        print("Pressed:" + " " + event.keysym)
        if (event.keysym == "w" or event.keysym == "Up"):
            self.snake.changeDirection('Up')
        if (event.keysym == "s" or event.keysym == "Down"):
            self.snake.changeDirection('Down')
        if (event.keysym == "a" or event.keysym == "Left"):
                self.snake.changeDirection('Left')
        if (event.keysym == "d" or event.keysym == "Right"):
                self.snake.changeDirection('Right')
        #if (event.keysym == "p"):

    def initgame(self):
        self.score = 0
        self.snake = (self.blocksize)
        self.food = Food(self.width, self.height,self.blocksize)

    # Start from this line are related to Game Design Patter
    def keepRunning(self):
        self.update()
        self.render()
        self.frame.after(50, self.keepRunning)

    def check_food(self):
        # check eating food
        if self.snake.pos[-1] == [self.food.x, self.food.y]:
            self.food = Food(self.width, self.height, self.blocksize)
            self.snake.grow()
            self.score += 10
            eatsound = pygame.mixer.Sound("bite.wav")
            pygame.mixer.play(eatsound)

    def check_boundary(self):
        # Left Boundary
        if self.snake.pos[-1][0] == -1:
            self.snake.pos[-1][0] = self.width - 1
        # Up Boundary
        if self.snake.pos[-1][1] == -1:
            self.snake.pos[-1][1] = self.height - 1
        # Right boundary
        if self.snake.pos[-1][0] == self.width:
            self.snake.pos[-1][0] = 0
        # Down boundary
        if self.snake.pos[-1][1] == self.height:
            self.snake.pos[-1][1] = 0

    def update(self):
        self.snake.update()
        self.food.update()
        self.check_food()
        self.check_boundary()
        #check eating itself
        pass

    def render(self):
        self.canvas.delete(ALL)
        self.snake.render(self.canvas)
        self.food.render(self.canvas)
        # initialize the score
        self.canvas.create_text(80,30,text = "Score: {}".format(self.score), fill = "#FF0099", font=font.Font(size= 30))

        #check eating self for game over
        if self.snake.pos[-1] in self.snake.pos[:-1]:
            self.frame.destroy()
            self.canvas.create_text(30, 30, text="Game Over!", fill="#2D7AE8", font=font.Font(size=40))




launcher = Launcher(40, 40)
launcher.keepRunning()
launcher.frame.mainloop()
print("After mainloop")
