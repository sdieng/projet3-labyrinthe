"""Pygame importation."""
import pygame
from pygame.locals import *


class Player:
    """
    Description.

    A class to define the attributes of the player.
    """

    def __init__(self):
        """Constructor. Sets blank coordinates and 'player.png' as sprite."""
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load('graphics/player.png').convert_alpha()

    # Getsetters
    def get_coord(self):
        """Return the player's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set the player's coordniates. Uses a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return player's sprite."""
        return self.sprite

    def empty(self):
        """Only for aesthetical purposes : makes the player's sprite invisible when he loses."""
        self.sprite = pygame.image.load('graphics/empty.png').convert_alpha()


class Exit:
    """
    Description.

    A class for the exit.
    Same as Player, but wanted to create one because it will be easier for future customization.
    """

    def __init__(self):
        """Constructor. Sets blank coordinates and 'exit.png' as sprite."""
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load('graphics/exit.png').convert_alpha()

    # Getsetters
    def get_coord(self):
        """Return the exit's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set the exit's coordniates. Uses a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return exit's sprite."""
        return self.sprite

    def empty(self):
        """Only for aesthetical purposes : makes the exit's sprite invisible."""
        self.sprite = pygame.image.load('graphics/empty.png').convert_alpha()


class Coordinates:
    """
    Description.

    Class to create an object to stock the coordinates of the various elements.
    """

    def __init__(self, x, y):
        """Constructor. Takes two values to set the coordinates : x and y."""
        self.x = x
        self.y = y

    # def setCoord(self, x, y):
        # self.x = x
        # self.y = y

    def get_x(self):
        """Return the x value of the coordinates."""
        return self.x

    def get_y(self):
        """Return the y value of the coordinates."""
        return self.y


class Square:
    """
    Description.

    A class that will define the squares of the maze.
    """

    def __init__(self, coord, is_wall):
        """Use Coordinates and isWall boolean as arguments. Starts with no item on it."""
        self.is_wall = is_wall
        self.coord = coord
        self.has_item = False
        self.item = Item(None, 'graphics/empty.png')

    # Getsetters
    def get_is_wall(self):
        """Return a boolean to know if the square is a wall."""
        return self.is_wall

    def get_has_item(self):
        """Return a boolean to know if there's an item on the square."""
        return self.has_item

    def set_has_item(self, state):
        """Set the state of the has_item boolean."""
        self.has_item = state

    def get_coord(self):
        """Return the square's position as a Coordinate type object."""
        return self.coord

    def set_item(self, item):
        """Change the Item attribute of the square. Uses an Item type object."""
        self.item = item

    def get_item(self):
        """Return the item on the square."""
        return self.item


class Item:
    """
    Description.

    A class to define the items of the maze.
    """

    def __init__(self, name, sprite):
        """Constructor. Name and sprite (file name) as arguments."""
        self.name = name
        self.got_item = False
        self.coord = Coordinates(None, None)
        self.sprite = pygame.image.load(sprite).convert_alpha()

    # Getsetters
    def get_got_item(self):
        """Return the got_item boolean to know if the player already got the item."""
        return self.got_item

    def set_got_item(self, state):
        """Set the got_item boolean to the state indicated by the argument."""
        self.got_item = state

    def get_coord(self):
        """Return the item's position as a Coordinate type object."""
        return self.coord

    def set_coord(self, coord):
        """Set the item's coordniates. Use a Coordinate type object as argument."""
        self.coord = coord

    def get_sprite(self):
        """Return item's sprite."""
        return self.sprite
