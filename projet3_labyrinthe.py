# -*- coding: utf-8 -*-

###############
##Import zone##
###############

import pygame
from pygame.locals import *
import random

from classes import *
from methods import *

###############
##Main method##
###############

def main():
	#Initialization of pygame
	pygame.init()

	#Initialization window and graphic library
	window = pygame.display.set_mode((450, 450))
	background = pygame.image.load('graphics/background.jpg').convert()
	wall = pygame.image.load('graphics/wall.png').convert()
	win = pygame.image.load('graphics/win.png').convert()
	lose = pygame.image.load('graphics/lose.png').convert()

	#Initialization of the player, grid and exit
	player = Player()
	exit = Exit()
	grid = generateGrid(player, exit)

	#Item creation and insertion in grid
	#Item no.1
	needle = Item("Needle", 'graphics/item1.png')
	needle.setCoord(generateRandomCoordinates())
	grid = putItemInGrid(grid, needle, player, exit)

	#Item no.2
	ether = Item("Ether", 'graphics/item2.png')
	ether.setCoord(generateRandomCoordinates())
	grid = putItemInGrid(grid, ether, player, exit)

	#Item no.3
	tube = Item("Tube", 'graphics/item3.png')
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


main()
