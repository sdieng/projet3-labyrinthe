##################################################################################
## A faire : contrôle des données,  navigation dans la grille (liste de Square) ##
##           interface graphique, capture d'événements (déplacement et fin)     ##
##################################################################################

##Zone des modules importés

import random

##Zone des classes crées

##Classe Coordinates qui est définie par deux entiers : x et y.
##Elle permet de stocker les coordonnées d'une case ou d'un objet
class Player:
	def __init__(self, coord):
		self.coord = coord

class Coordinates:

	def __init__(self, x, y):
		self.x = x
		self.y = y

##Classe qui définit les cases de l'aire de jeu.

class Square:

	def __init__(self, coord, isWall): ##, hasItem, item
		self.isWall = isWall
		self.coord = coord
		self.hasItem = False
		self.item = Item('test')

	##Getsetters

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
	##Créer méthode pour savoir si la case contient un objet en parcourant une liste d'objets et en comparant l'attribut coord
	##des deux. If square.coord == item.coord, then item.gotItem = True. A lancer après mouvement


##Classe définissant les objets du jeu par leur nom, leur emplacement, et un booléen qui indique si l'objet est en notre possession.

class Item:
	def __init__(self, name):
		self.name = name
		self.gotItem = False

	#Getsetters

	def getGotItem(self):
		return self.gotItem

	def setGotItem(state):
		self.gotItem = state

##Bloc main

def main():
	macgyver = Player(Coordinates(8, 1))
	grid = generateGrid()
	## Zone de tests
	print(grid[0].isWall)
	print(grid[7].isWall)
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

##Méthode générale pour générer des coordonnées aléatoires.
##Renvoie un objet de type Coordinates

def generateRandomCoordinates():
	coord = Coordinates(random.randint(0, 14), random.randint(0, 14))
	return coord

#Méthode de génération de la grille

def generateGrid():
	with open('grid.txt') as txtgrid:
	    strgrid = ''.join(line.strip() for line in txtgrid)
	    chrlistGrid = list(strgrid)
	    grid = []
	    x = 0
	    y = 0
	    ##Lire la chaîne par caractères, créer un Square par caractère (for) en définissant isWall selon le caractère lu
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
