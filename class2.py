from tkinter import *
import random
# #include<tkinter.h>
class Ball:

    def __init__(self, width, height):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.dx = random.randrange(-5, 5, 1)
        self.dy = random.randrange(-5, 5, 1)
        self.color = random.choice(["#FFEE78", "#22FFFF", "#FF00FF"])

    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def render(self):
        pass




class Box:
    def __init__(self,x,y,dx,dy):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy

    def update(self):
        self.x +=self.dx
        self.y+=self.dy


    def render(self, canvas):
        assert (isinstance(canvas, Canvas))
        canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="#FFFFFF")



class Launcher:

    def __init__(self, width, height):
        self.frame = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.frame, width = self.width, height = self.height, bg = "#545454")
        self.canvas.pack()
        # <Key> is predefined by the librart tKinter
        # self.keyboardInput is a function, not a function call, so there's no parentheses
        self.frame.bind("<Key>", self.keyboardInput)
        ## properties about game objects
        self.box= Box(150,150,2,2)
        self.ball=Ball(20,30)
        self.ballLst = []

    #This is the Event Funtions
    def keyboardInput(self, event):
       if (event.keysym == "w" or event.keysym == "Up"):
           self.box.dy += -1
       if (event.keysym == "s" or event.keysym == "Down"):
           self.box.dy += 1
       if (event.keysym == "a" or event.keysym == "Left"):
           self.box.dy += -1
       if (event.keysym == "d" or event.keysym == "Right"):
           self.box.dy += 1

    def run(self):
        self.update()
        self.render()
        self.frame.after(50, self.run)

    def update(self):
        self.box.update()
        pass

    # For this render inside the Launcher, it delete everything
    #on the canvas. And then call the render function inside the Box class to paint
    #a new box
    def render(self):
        self.canvas.delete(ALL)
        self.box.render(self.canvas)
        pass

launcher = Launcher(800, 600)
launcher.run()
launcher.frame.mainloop()