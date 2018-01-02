# -*- coding: utf-8 -*-
##################################################################################
## A faire : contrôle des données, capture d'événements (déplacement et fin)    ##
##################################################################################

##Import zone
import pygame
from pygame.locals import *
import random

##Custom classes

#A class to define the attributes of the player
class Player:
	def __init__(self, coord):
		self.coord = coord

	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, x, y):
		self.coord.x = x
		self.coord.y = y

#A class to stock the coordinates of a square, player or item
class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

#A class that will define the squares of the maze
class Square:
	def __init__(self, coord, isWall): ##, hasItem, item
		self.isWall = isWall
		self.coord = coord
		self.hasItem = False
		self.item = Item('test')

	#Getsetters

	def getIsWall(self):
		return self.isWall

	def setIsWall(state):
		self.isWall = state

	def getHasItem(self):
		return self.hasItem

	def setHasItem(state):
		self.hasItem = state

	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, x, y):
		self.coord.x = x
		self.coord.y = y

	def setItem(self, item):
		self.item = item

    #Method to check if the movement input is valid (not a wall) and to get
	#the item on the square if there is one
	def checkMove(grid, player, coord):
		for square in grid:
			if square.coord == coord:
				if square.getIsWall() == False:
					player.setCoord(coord)
					if square.getHasItem() == True:
						square.item.setGotItem(True)

#A class to define the items by a name and a boolean to know if the player
#got the item
class Item:
	def __init__(self, name):
		self.name = name
		self.gotItem = False

	#Getsetters

	def getGotItem(self):
		return self.gotItem

	def setGotItem(state):
		self.gotItem = state

##Main method

def main():
	#Initialization of pygame
	pygame.init()

	#Initialization window and graphic library
	window = pygame.display.set_mode((450, 450))
	background = pygame.image.load("background.jpg").convert()
	wall = pygame.image.load("wall.png").convert()
	window.blit(background,(0, 0))

	#Initialization of the player and the grid
	player = Player(Coordinates(8, 1))
	grid = generateGrid()

	#Display of the maze
	count = 0
	pos_x = 0
	pos_y = 0

	for square in grid:
		if count < 15:
			if square.isWall == True:
				print("(" + str(pos_x) + " ; " + str(pos_y) + ")")
				window.blit(wall, (pos_x, pos_y))
				pos_x += 30
				count += 1
				if count == 15:
					count = 0
					pos_x = 0
					pos_y += 30

			else:
				pos_x += 30
				count += 1
				if count == 15:
					count = 0
					pos_x = 0
					pos_y += 30

		pygame.display.flip()

	##Event capture zone
	running = 1
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = 0

	##Test zone
	##print(grid[0].isWall)
	##print(grid[7].isWall)
	##case = Square(generateRandomCoordinates(), False)
	##print(case.coord.x)
	##print(case.coord.y)
	##print(case)
	##print(case.item.name)
	##print(case.item.coord.x)
	##print(case.item.coord.y)
	##case.setCoord(1, 1)
	##case.item.setCoord(2, 2)
	##print(case.coord.x)
	##print(case.coord.y)
	##print(case.item.coord.x)
	##print(case.item.coord.y)

#Method to get random coordinates. Returns a Coordinates type object
def generateRandomCoordinates():
	coord = Coordinates(random.randint(0, 14), random.randint(0, 14))
	return coord

#Method to generate the grid
def generateGrid():
	with open('grid.txt') as txtgrid:
	    strgrid = ''.join(line.strip() for line in txtgrid)
	    chrlistGrid = list(strgrid)
	    grid = []
	    x = 0
	    y = 0

	    for entry in chrlistGrid:
		    coord = Coordinates(x, y)

		    if entry == 'W':
			    grid.append(Square(coord, True))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

		    elif entry == 'X':
			    grid.append(Square(coord, False))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

	##syringe = Item('seringue')
	##tube = Item('tube')
	##needle = Item('aiguille')
	return grid


main()
