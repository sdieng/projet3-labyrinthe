# -*- coding: utf-8 -*-
#######################################################################
## A faire :  nettoyer code, attention aux getsetters, commenter     ##
#######################################################################

##Import zone
import pygame
from pygame.locals import *
import random

##Custom classes

#A class to define the attributes of the player
class Player:
	def __init__(self):
		self.coord = None
		self.image = pygame.image.load("player.png").convert_alpha()

	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, coord):
		self.coord = coord

	def getImage(self):
		return self.image

	def empty(self):
		self.image = pygame.image.load("empty.png").convert_alpha()

class Exit:
	def __init__(self):
		self.coord = None
		self.image = pygame.image.load("exit.png").convert_alpha()

	def getCoord(self):
		x = self.coord.x
		y = self.coord.y
		return Coordinates(x, y)

	def setCoord(self, coord):
		self.coord = coord

	def getImage(self):
		return self.image

	def empty(self):
		self.image = pygame.image.load("empty.png").convert_alpha()

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
		self.item = Item(None)

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


#A class to define the items by a name and a boolean to know if the player
#got the item
class Item:
	def __init__(self, name):
		self.name = name
		self.gotItem = False
		self.coord = Coordinates(None, None)
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
	win = pygame.image.load("win.png").convert()
	lose = pygame.image.load("lose.png").convert()

	#Initialization of the player and the grid
	player = Player()
	exit = Exit()
	grid = generateGrid(player, exit)
	print("Exit at " + str(exit.getCoord().getX()) + ";" + str(exit.getCoord().getY()))

	needle = Item("Needle")
	needle.setImage("item1.png")
	print(str(needle.coord.x) + ";" + str(needle.coord.y))
	needle.coord = generateRandomCoordinates()

	grid = putItemInGrid(grid, needle, player, exit)


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
	displayGrid(grid, window, wall, background, exit, player)

	##Event capture zone

	running = 1
	capture = 1
	itemCount = 0

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				capture = 0
				running = 0
		while capture:
			for event in pygame.event.get():
				if event.type == QUIT:
					capture = 0
					running = 0

				#Movement
				if event.type == KEYDOWN:
					if event.key == K_DOWN:
						for square in grid:
							if square.coord.y == (player.coord.y + 1) and square.coord.x == player.coord.x and square.isWall == False:
								print("OK MOVE")
								print(str(square.coord.x) + ";" + str(square.coord.y))
								player.setCoord(Coordinates(square.coord.x, square.coord.y))
								displayGrid(grid, window, wall, background, exit, player)
								if square.hasItem == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
									print("Got Item no." + str(itemCount))
								pygame.display.flip()
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										print("You win !!!")
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										print("You lose !!!")
										capture = 0
								break

					if event.key == K_UP:
						for square in grid:
							if square.coord.y == (player.coord.y - 1) and square.coord.x == player.coord.x and square.isWall == False:
								print("OK MOVE")
								print(str(square.coord.x) + ";" + str(square.coord.y))
								player.setCoord(Coordinates(square.coord.x, square.coord.y))
								displayGrid(grid, window, wall, background, exit, player)
								if square.hasItem == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
									print("Got Item no." + str(itemCount))
								pygame.display.flip()
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										print("You win !!!")
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										print("You lose !!!")
										capture = 0
								break

					if event.key == K_LEFT:
						for square in grid:
							if square.coord.x == (player.coord.x - 1) and square.coord.y == player.coord.y and square.isWall == False:
								print("OK MOVE")
								print(str(square.coord.x) + ";" + str(square.coord.y))
								player.setCoord(Coordinates(square.coord.x, square.coord.y))
								displayGrid(grid, window, wall, background, exit, player)
								if square.hasItem == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
									print("Got Item no." + str(itemCount))
								pygame.display.flip()
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										print("You win !!!")
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										print("You lose !!!")
										capture = 0
								break

					if event.key == K_RIGHT:
						for square in grid:
							if square.coord.x == (player.coord.x + 1) and square.coord.y == player.coord.y and square.isWall == False:
								print("OK MOVE")
								print(str(square.coord.x) + ";" + str(square.coord.y))
								player.setCoord(Coordinates(square.coord.x, square.coord.y))
								displayGrid(grid, window, wall, background, exit, player)
								if square.hasItem == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
									print("Got Item no." + str(itemCount))
								pygame.display.flip()
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										print("You win !!!")
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										print("You lose !!!")
										capture = 0
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
			    exit.setCoord(Coordinates(x, y))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

	return grid

#Method to display the grid
def displayGrid(grid, window, wall, background, exit, player):
		window.blit(background, (0, 0))
		window.blit(player.getImage(), (player.getCoord().x * 30, player.getCoord().y * 30))
		window.blit(exit.getImage(), (exit.getCoord().getX() * 30, exit.getCoord().getY() * 30))

		for square in grid:
			if square.isWall == True:
				window.blit(wall, (square.getCoord().getX() * 30, square.getCoord().getY() * 30))

			else:
				if square.hasItem == True:
					window.blit(square.getItem().getImage(), (square.coord.x * 30, square.coord.y * 30))
		pygame.display.flip()

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
