# -*- coding: utf-8 -*-

###############
##Import zone##
###############

import pygame
from pygame.locals import *
import random

###########
##Classes##
###########

#A class to define the attributes of the player
class Player:
	def __init__(self):
		self.coord = Coordinates(None, None)
		self.sprite = pygame.image.load('player.png').convert_alpha()

	#Getsetters
	def getCoord(self):
		return self.coord

	def setCoord(self, coord):
		self.coord = coord

	def getSprite(self):
		return self.sprite

	#A method only for aesthetical purposes : makes the player's sprite invisible when he loses
	def empty(self):
		self.sprite = pygame.image.load('empty.png').convert_alpha()

#A class for the exit. Same as Player, but wanted to create one because it will be easier for future customization
class Exit:
	def __init__(self):
		self.coord = Coordinates(None, None)
		self.sprite = pygame.image.load('exit.png').convert_alpha()

	#Getsetters
	def getCoord(self):
		return self.coord

	def setCoord(self, coord):
		self.coord = coord

	def getSprite(self):
		return self.sprite

	#A method only for aesthetical purposes : makes the exit's sprite invisible when he wins
	def empty(self):
		self.sprite = pygame.image.load('empty.png').convert_alpha()

#Class to create an object to stock the coordinates of the various elements (player, exit, squares)
class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

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
		self.item = Item(None, 'empty.png')

	#Getsetters
	def getIsWall(self):
		return self.isWall

	def getHasItem(self):
		return self.hasItem

	def setHasItem(self, state):
		self.hasItem = state

	def getCoord(self):
		return self.coord

	def setItem(self, item):
		self.item = item

	def getItem(self):
		return self.item


#A class to define the items
class Item:
	def __init__(self, name, sprite):
		self.name = name
		self.gotItem = False
		self.coord = Coordinates(None, None)
		self.sprite = pygame.image.load(sprite).convert_alpha()

	#Getsetters
	def getGotItem(self):
		return self.gotItem

	def setGotItem(self, state):
		self.gotItem = state

	def getCoord(self):
		return self.coord

	def setCoord(self, coord):
		self.coord = coord

	def getSprite(self):
		return self.sprite

###############
##Main method##
###############

def main():
	#Initialization of pygame
	pygame.init()

	#Initialization window and graphic library
	window = pygame.display.set_mode((450, 450))
	background = pygame.image.load('background.jpg').convert()
	wall = pygame.image.load('wall.png').convert()
	win = pygame.image.load('win.png').convert()
	lose = pygame.image.load('lose.png').convert()

	#Initialization of the player, grid and exit
	player = Player()
	exit = Exit()
	grid = generateGrid(player, exit)

	#Item creation and insertion in grid
	#Item no.1
	needle = Item("Needle", 'item1.png')
	needle.setCoord(generateRandomCoordinates())
	grid = putItemInGrid(grid, needle, player, exit)

	#Item no.2
	ether = Item("Ether", 'item2.png')
	ether.setCoord(generateRandomCoordinates())
	grid = putItemInGrid(grid, ether, player, exit)

	#Item no.3
	tube = Item("Tube", 'item3.png')
	tube.setCoord(generateRandomCoordinates())
	grid = putItemInGrid(grid, tube, player, exit)

	#Display of the grid
	displayGrid(grid, window, wall, background, exit, player)

	#################
	##Event capture##
	#################

	running = 1
	capture = 1
	itemCount = 0
	pygame.key.set_repeat(400, 30)

	#2 loops : one solely for the capture of events, so movements can be disabled when game is over
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

				#Movement by event capture
				if event.type == KEYDOWN:
					if event.key == K_DOWN:
						for square in grid:
							#Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
							if square.getCoord().getY() == (player.getCoord().getY() + 1) and square.getCoord().getX() == player.getCoord().getX() and square.getIsWall() == False:
								player.setCoord(square.getCoord())
								displayGrid(grid, window, wall, background, exit, player)
								#Checks if there's an item on the square, and picks it if the condition is true
								if square.getHasItem() == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
								pygame.display.flip()
								#Checks if the square is the exit, and if it is, checks if the player has all the items
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									#Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										capture = 0
								break

					if event.key == K_UP:
						for square in grid:
							#Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
							if square.getCoord().getY() == (player.getCoord().getY() - 1) and square.getCoord().getX() == player.getCoord().getX() and square.getIsWall() == False:
								player.setCoord(square.getCoord())
								displayGrid(grid, window, wall, background, exit, player)
								#Checks if there's an item on the square, and picks it if the condition is true
								if square.hasItem == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
								pygame.display.flip()
								#Checks if the square is the exit, and if it is, checks if the player has all the items
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									#Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										capture = 0
								break

					if event.key == K_LEFT:
						for square in grid:
							#Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
							if square.getCoord().getX() == (player.getCoord().getX() - 1) and square.getCoord().getY() == player.getCoord().getY() and square.getIsWall() == False:
								player.setCoord(square.getCoord())
								displayGrid(grid, window, wall, background, exit, player)
								#Checks if there's an item on the square, and picks it if the condition is true
								if square.getHasItem() == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
								pygame.display.flip()
								#Checks if the square is the exit, and if it is, checks if the player has all the items
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									#Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										capture = 0
								break

					if event.key == K_RIGHT:
						for square in grid:
							#Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
							if square.getCoord().getX() == (player.getCoord().getX() + 1) and square.getCoord().getY() == player.getCoord().getY() and square.getIsWall() == False:
								player.setCoord(square.getCoord())
								displayGrid(grid, window, wall, background, exit, player)
								#Checks if there's an item on the square, and picks it if the condition is true
								if square.getHasItem() == True:
									itemCount += 1
									square.setHasItem(False)
									square.getItem().setGotItem(True)
									displayGrid(grid, window, wall, background, exit, player)
								pygame.display.flip()
								#Checks if the square is the exit, and if it is, checks if the player has all the items
								if player.getCoord().getX() == exit.getCoord().getX() and player.getCoord().getY() == exit.getCoord().getY():
									#Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
									if itemCount == 3:
										exit.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(win, (0, 150))
										pygame.display.flip()
										capture = 0
									else:
										player.empty()
										displayGrid(grid, window, wall, background, exit, player)
										window.blit(lose, (0, 150))
										pygame.display.flip()
										capture = 0
								break

###################
##General methods##
###################

#Method to get random coordinates. Returns a Coordinates type object
def generateRandomCoordinates():
	return Coordinates(random.randint(0, 14), random.randint(0, 14))

#Method to generate the grid : transforms the .txt file into a list of lines, then each line into a list of characters
def generateGrid(player, exit):
	with open('grid.txt') as txtgrid:
	    strgrid = ''.join(line.strip() for line in txtgrid)
	    chrlistGrid = list(strgrid)
	    grid = []
	    x = 0
	    y = 0

	    for entry in chrlistGrid:
			#Sets square as a wall if the character is 'W'
		    if entry == 'W' or entry == 'w':
			    grid.append(Square(Coordinates(x, y), True))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

		    elif entry == 'X' or entry == 'x':
				#Sets square as empty if the character is 'X'
			    grid.append(Square(Coordinates(x, y), False))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

		    elif entry == 'S' or entry == 's':
				#Sets the inital position of the player if the character is a 'S'
			    grid.append(Square(Coordinates(x, y), False))
			    player.setCoord(Coordinates(x, y))
			    if x < 14:
				    x = x + 1

			    elif x == 14:
				    x = 0
				    y = y + 1

		    elif entry == 'E' or entry == 'e':
				#Sets the position of the exit if the character is a 'E'
			    grid.append(Square(Coordinates(x, y), False))
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
		window.blit(player.getSprite(), (player.getCoord().getX() * 30, player.getCoord().getY() * 30))
		window.blit(exit.getSprite(), (exit.getCoord().getX() * 30, exit.getCoord().getY() * 30))

		for square in grid:
			if square.isWall == True:
				window.blit(wall, (square.getCoord().getX() * 30, square.getCoord().getY() * 30))

			else:
				if square.hasItem == True:
					window.blit(square.getItem().getSprite(), (square.getCoord().getX() * 30, square.getCoord().getY() * 30))
		pygame.display.flip()

#Method to put the items in the grid, at random positions
def putItemInGrid(grid, item, player, exit):
	for square in grid:
		if square.getCoord().getX() == item.getCoord().getX() and square.getCoord().getY() == item.getCoord().getY():
			if (item.getCoord().getX() != exit.getCoord().getX() and item.getCoord().getY() != exit.getCoord().getY()) and (item.getCoord().getX() != player.getCoord().getX() and item.getCoord().getY() != player.getCoord().getY()):
				if square.getHasItem() == True:
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
