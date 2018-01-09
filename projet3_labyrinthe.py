# -*- coding: utf-8 -*-
#############################################################
## A faire :  condition victoire                           ##
#############################################################

##Import zone
import pygame
from pygame.locals import *
import random

##Custom classes

#A class to define the attributes of the player
class Player:
	def __init__(self, coord):
		self.coord = coord
		self.image = pygame.transform.scale(pygame.image.load("player.png").convert_alpha(), (30, 30))
		self.position = self.image.get_rect()


	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, coord):
		self.coord = coord

#A class to stock the coordinates of a square, player or item
class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getCoord(self):
		x = self.x
		y = self.y
		return Coordinates(x, y)

	def setCoord(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

#A class that will define the squares of the maze
class Square:
	def __init__(self, coord, isWall): ##, hasItem, item
		self.isWall = isWall
		self.coord = coord
		self.hasItem = False
		self.item = Item('null')

	#Getsetters

	def getIsWall(self):
		return self.isWall

	def setIsWall(self, state):
		self.isWall = state

	def getHasItem(self):
		return self.hasItem

	def setHasItem(self, state):
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

	def getItem(self):
		return self.item


    #Method to check if the movement input is valid (not a wall) and to get
	#the item on the square if there is one (DELETE)
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
		self.coord = Coordinates(0, 0)
		self.image = None

	#Getsetters

	def getGotItem(self):
		return self.gotItem

	def setGotItem(self, state):
		self.gotItem = state

	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, coord):
		self.coord = coord

	def getImage(self):
		return self.image

	def setImage(self, image):
		self.image = pygame.image.load(image).convert_alpha()

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
	player = Player(Coordinates(8, 13))
	exit = Coordinates(0, 0)
	tp = pygame.image.load("player.png").convert_alpha()


	grid = generateGrid(player, exit)

	needle = Item("Needle")
	needle.setImage("item1.png")
	print(str(needle.coord.x) + ";" + str(needle.coord.y))
	needle.coord = generateRandomCoordinates()
	#for square in grid:
		#if square.coord.x == needle.coord.x and square.coord.y == needle.coord.y:
			#print(square.isWall)
			#print(square.hasItem)
	#print(str(needle.coord.x) + ";" + str(needle.coord.y))
	grid = putItemInGrid(grid, needle, player, exit)
	#for square in grid:
		#if square.coord.x == needle.coord.x and square.coord.y == needle.coord.y:
			#print(square.isWall)
			#print(square.hasItem)
	#print(str(needle.coord.x) + ";" + str(needle.coord.y))

	ether = Item("Ether")
	ether.setImage("item2.png")
	ether.coord = generateRandomCoordinates()
	grid = putItemInGrid(grid, ether, player, exit)

	tube = Item("Tube")
	tube.setImage("item3.png")
	tube.coord = generateRandomCoordinates()
	grid = putItemInGrid(grid, tube, player, exit)

	for square in grid:
		if square.hasItem == True:
			print(str(square.coord.x) + ";" + str(square.coord.y) + "has an item")

	#Display of the grid
	displayGrid(grid, window, wall, background)
	window.blit(tp, (player.getCoord().x * 30, player.getCoord().y * 30))
	tppos = tp.get_rect()
	pygame.display.flip()

	##Event capture zone
	running = 1
	itemCount = 0
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = 0

			#Movement
			if event.type == KEYDOWN:
				if event.key == K_DOWN:
					for square in grid:
						if square.coord.y == (player.coord.y + 1) and square.coord.x == player.coord.x and square.isWall == False:
							print("OK MOVE")
							print(str(square.coord.x) + ";" + str(square.coord.y))
							displayGrid(grid, window, wall, background)
							player.setCoord(Coordinates(square.coord.x, square.coord.y))
							tppos.move(0, 30)
							window.blit(tp, (player.coord.x * 30, player.coord.y * 30))
							if square.hasItem == True:
								itemCount += 1
								square.setHasItem(False)
								square.getItem().setGotItem(True)
								print("Got Item no." + str(itemCount))
							pygame.display.flip()
							break

				if event.key == K_UP:
					for square in grid:
						if square.coord.y == (player.coord.y - 1) and square.coord.x == player.coord.x and square.isWall == False:
							print("OK MOVE")
							print(str(square.coord.x) + ";" + str(square.coord.y))
							displayGrid(grid, window, wall, background)
							player.setCoord(Coordinates(square.coord.x, square.coord.y))
							tppos.move(0, -30)
							window.blit(tp, (player.coord.x * 30, player.coord.y * 30))
							if square.hasItem == True:
								itemCount += 1
								square.setHasItem(False)
								square.getItem().setGotItem(True)
								print("Got Item no." + str(itemCount))
							pygame.display.flip()
							break

				if event.key == K_LEFT:
					for square in grid:
						if square.coord.x == (player.coord.x - 1) and square.coord.y == player.coord.y and square.isWall == False:
							print("OK MOVE")
							print(str(square.coord.x) + ";" + str(square.coord.y))
							displayGrid(grid, window, wall, background)
							player.setCoord(Coordinates(square.coord.x, square.coord.y))
							tppos.move(-30, 0)
							window.blit(tp, (player.coord.x * 30, player.coord.y * 30))
							if square.hasItem == True:
								itemCount += 1
								square.setHasItem(False)
								square.getItem().setGotItem(True)
								print("Got Item no." + str(itemCount))
							pygame.display.flip()
							break

				if event.key == K_RIGHT:
					for square in grid:
						if square.coord.x == (player.coord.x + 1) and square.coord.y == player.coord.y and square.isWall == False:
							print("OK MOVE")
							print(str(square.coord.x) + ";" + str(square.coord.y))
							displayGrid(grid, window, wall, background)
							player.setCoord(Coordinates(square.coord.x, square.coord.y))
							tppos.move(30, 0)
							window.blit(tp, (player.coord.x * 30, player.coord.y * 30))
							if square.hasItem == True:
								itemCount += 1
								square.setHasItem(False)
								square.getItem().setGotItem(True)
								print("Got Item no." + str(itemCount))
							pygame.display.flip()
							break

	##Test zone

#Method to get random coordinates. Returns a Coordinates type object
def generateRandomCoordinates():
	coord = Coordinates(random.randint(0, 14), random.randint(0, 14))
	return coord

#Method to generate the grid
def generateGrid(player, exit):
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

		    elif entry == 'S':
			    grid.append(Square(coord, False))
			    player.setCoord(Coordinates(x, y))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

		    elif entry == 'E':
			    grid.append(Square(coord, False))
			    exit.setCoord(x, y)
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

	##syringe = Item('ether')
	##tube = Item('tube')
	##needle = Item('aiguille')
	return grid

#Method to display the grid
def displayGrid(grid, window, wall, background):
		window.blit(background, (0, 0))

		for square in grid:
			if square.isWall == True:
				window.blit(wall, (square.getCoord().getX() * 30, square.getCoord().getY() * 30))

			else:
				if square.hasItem == True:
					window.blit(square.getItem().getImage(), (square.coord.x * 30, square.coord.y * 30))

def putItemInGrid(grid, item, player, exit):
	for square in grid:
		if square.getCoord().x == item.getCoord().x and square.getCoord().y == item.getCoord().y:
			if (item.getCoord().x != exit.getCoord().x and item.getCoord().y != exit.getCoord().y) and (item.getCoord().x != player.getCoord().x and item.getCoord().y != player.getCoord().y):
				if square.hasItem == True:
					item.setCoord(generateRandomCoordinates())
					putItemInGrid(grid, item, player, exit)
					break
				if square.getIsWall() == True:
					item.setCoord(generateRandomCoordinates())
					putItemInGrid(grid, item, player, exit)
					break
				if square.getIsWall() == False and square.getHasItem() == False:
					square.setHasItem(True)
					square.setItem(item)
					break
			else:
				item.setCoord(generateRandomCoordinates())
				putItemInGrid(grid, item, player, exit)
				break

	return grid

main()
