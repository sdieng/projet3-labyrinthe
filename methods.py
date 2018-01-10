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
