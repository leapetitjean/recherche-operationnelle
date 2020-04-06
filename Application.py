#imports 
from tkinter import *
from Algorithm import Algorithm
from CloseNeighbor import CloseNeighbor
from NearInsertion import NearInsertion
from FarInsertion import FarInsertion
from Genetic import Genetic

class Application():
    """ Représente une application avec les villes et les algorithmes correspondant """
    def __init__(self, tour):
        self.algo = Algorithm(tour)
        self.tour = self.algo.getTour()
        self.t0 = self.tour
        self.rangeX = self.getMaxX()-self.getMinX()
        self.rangeY = self.getMaxY()-self.getMinY()
        #création fenêtre
        self.root = Tk()
        self.root.title("Voyage en Côte d'Or")
        self.root.resizable(0,0)
        #dimensions canvas
        self.width = 1000
        self.height = 350
        #création canvas
        self.c = Canvas(self.root, bg="lightblue", width = self.width+100, height = self.height+100)
        #photo = PhotoImage(file=imagePath)
        #self.c.create_image(0, -80, anchor='nw', image=photo)
        self.c.configure(cursor="arrow")
        self.c.grid(row = 1, column = 1, columnspan = 7)

        Button(self.root, fg = "black", bg = "indianred", text = "CLEAR", command = self.clear).grid(row = 2, rowspan = 4, column = 6, columnspan = 2, sticky = 'nsew')
        Button(self.root, fg = "white", bg = "blue", text = "numbers", command = self.drawCities).grid(row = 2, column = 1, sticky = 'ew')
        Button(self.root, fg = "white", bg = "blue", text = "names", command = self.drawNames).grid(row = 2, column = 2, sticky = 'ew')
        Button(self.root, text = "Algorithme Shuffle", command = self.shuffle).grid(row = 3, column = 1, sticky = 'ew')
        Button(self.root, text = "Algorithme CloseNeighbor", command = self.closeNeighbor).grid(row = 3, column = 2, sticky = 'ew')
        Button(self.root, text = "Algorithme NearInsertion", command = self.nearInsertion).grid(row = 3, column = 3, sticky = 'ew')
        Button(self.root, text = "Algorithme FarInsertion", command = self.farInsertion).grid(row = 3, column = 4, sticky = 'ew')
        Button(self.root, text = "Algorithme Genetic", command = self.genetic).grid(row = 3, column = 5, sticky = 'ew')
        Button(self.root, text = "consecutive amelioration", command = self.consecutive).grid(row = 4, column = 1, sticky = 'ew')
        Button(self.root, text = "non consecutive amelioration", command = self.nonConsecutive).grid(row = 4, column = 2, sticky = 'ew')
        Button(self.root, text = "amelioration 2 opt", command = self.amelioration2opt).grid(row = 4, column = 3, sticky = 'ew')
        Button(self.root, text = "localResearch", command = self.localResearch).grid(row = 4, column = 4, sticky = 'ew')
        Button(self.root, text = "better consecutive amelioration", command = self.betterConsecutive).grid(row = 5, column = 1, sticky = 'ew')
        Button(self.root, text = "better non consecutive amelioration", command = self.betterNonConsecutive).grid(row = 5, column = 2, sticky = 'ew')
        self.root.mainloop()

    def localResearch(self):
        self.algo.localResearch()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()

    def consecutive(self):
        self.algo.consecutiveNeighborhood()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()

    def nonConsecutive(self):
        self.algo.nonConsecutiveNeighborhood()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()

    def betterConsecutive(self):
        self.algo.betterConsecutiveNeighborhood()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()

    def betterNonConsecutive(self):
        self.algo.betterNonConsecutiveNeighborhood()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()

    def amelioration2opt(self):
        self.algo.amelioration2opt()
        self.tour = self.algo.getTour()
        self.c.delete("point", "line", "cost")
        self.drawTour()


    def clear(self):
        self.c.delete("point", "line", "cost")
        self.algo = Algorithm(self.t0)
        self.tour = self.t0
        

    def getMinX(self):
        x = []
        for city in self.tour:
            x.append(city.getX())
        return min(x)

    def getMaxX(self):
        x = []
        for city in self.tour:
            x.append(city.getX())
        return max(x)

    def getMinY(self):
        y = []
        for city in self.tour:
            y.append(city.getY())
        return min(y)

    def getMaxY(self):
        y = []
        for city in self.tour:
            y.append(city.getY())
        return max(y)

    def shuffle(self):
        self.algo = Algorithm(self.tour)
        self.algo.execute()
        self.tour = self.algo.getTour()
        self.drawTour()

    def closeNeighbor(self):
        self.algo = CloseNeighbor(self.tour)
        self.algo.execute()
        self.tour = self.algo.getTour()
        self.drawTour()

    def nearInsertion(self):
        self.algo = NearInsertion(self.tour)
        self.algo.execute()
        self.tour = self.algo.getTour()
        self.drawTour()

    def farInsertion(self):
        self.algo = FarInsertion(self.tour)
        self.algo.execute()
        self.tour = self.algo.getTour()
        self.drawTour()

    def genetic(self):
        self.algo = Genetic(self.tour)
        self.algo.execute()
        self.tour = self.algo.getTour()
        self.drawTour()

    def drawTour(self):
        self.drawLines()
        self.drawCost()
        print(self.algo.__str__())

    def drawCost(self):
        self.c.create_text(800, 50, anchor="n", text="Coût : "+str(self.algo.cost()), font="Arial 8", fill="red", tags="cost")

    def drawLines(self):
        for i in range(0, len(self.tour)-1):
            self.drawLine(self.tour[i], self.tour[i+1])
        self.drawLine(self.tour[0], self.tour[len(self.tour)-1])

    def drawLine(self, city1, city2):
        self.c.create_line(self.convertX(city1.getX()), self.convertY(city1.getY()), self.convertX(city2.getX()), self.convertY(city2.getY()), tags="line")

    def drawCity(self, city):
        self.c.create_text(self.convertX(city.getX()), self.convertY(city.getY()), anchor="n", text=city.getNum(), font="Arial 8", fill="blue", tags="point")

    def drawName(self, city):
        self.c.create_text(self.convertX(city.getX()), self.convertY(city.getY()), anchor="n", text=city.getName(), font="Arial 8", fill="blue", tags="point")

    def convertX(self, x):
        return(int((x-self.getMinX())*self.width/self.rangeX)+50)

    def convertY(self, y):
        return(self.height-int((y-self.getMinY())*self.height/self.rangeY)+50)
    
    def drawCities(self):
        for city in self.tour:
            self.drawCity(city)

    def drawNames(self):        
        for city in self.tour:
            self.drawName(city)


