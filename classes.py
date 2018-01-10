###########
##Classes##
###########

#A class to define the attributes of the player
class Player:
	def __init__(self):
		self.coord = Coordinates(None, None)
		self.sprite = pygame.image.load('graphics/player.png').convert_alpha()

	#Getsetters
	def getCoord(self):
		return self.coord

	def setCoord(self, coord):
		self.coord = coord

	def getSprite(self):
		return self.sprite

	#A method only for aesthetical purposes : makes the player's sprite invisible when he loses
	def empty(self):
		self.sprite = pygame.image.load('graphics/empty.png').convert_alpha()

#A class for the exit. Same as Player, but wanted to create one because it will be easier for future customization
class Exit:
	def __init__(self):
		self.coord = Coordinates(None, None)
		self.sprite = pygame.image.load('graphics/exit.png').convert_alpha()

	#Getsetters
	def getCoord(self):
		return self.coord

	def setCoord(self, coord):
		self.coord = coord

	def getSprite(self):
		return self.sprite

	#A method only for aesthetical purposes : makes the exit's sprite invisible when he wins
	def empty(self):
		self.sprite = pygame.image.load('graphics/empty.png').convert_alpha()

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
		self.item = Item(None, 'graphics/empty.png')

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
