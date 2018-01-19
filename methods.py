"""Pygame, random and class file imoprtation."""
import random
import pygame
from pygame.locals import *
from classes import Coordinates, Square


def generate_random_coordinates():
    """Method to get random coordinates. Returns a Coordinates type object."""
    return Coordinates(random.randint(0, 14), random.randint(0, 14))


def generate_grid(player, exit):
    """
    Method to generate the grid.

    Transforms the .txt file into a list of lines, then each line into a list of characters.
    For each character it will generate a square, or set the player/exit's position.
    """
    with open('grid.txt') as txt_grid:
        str_grid = ''.join(line.strip() for line in txt_grid)
        chr_grid = list(str_grid)
        grid = []
        x = 0
        y = 0

        for entry in chr_grid:
            # Sets square as a wall if the character is 'W'
            if entry == 'W' or entry == 'w':
                grid.append(Square(Coordinates(x, y), True))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'X' or entry == 'x':
                # Sets square as empty if the character is 'X'
                grid.append(Square(Coordinates(x, y), False))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'S' or entry == 's':
                # Sets the inital position of the player if the character is a 'S'
                grid.append(Square(Coordinates(x, y), False))
                player.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

            elif entry == 'E' or entry == 'e':
                # Sets the position of the exit if the character is a 'E'
                grid.append(Square(Coordinates(x, y), False))
                exit.set_coord(Coordinates(x, y))
                if x < 14:
                    x = x + 1

                elif x == 14:
                    x = 0
                    y = y + 1

    return grid


def display_grid(grid, window, wall, background, exit, player):
    """Method to display the grid."""
    window.blit(background, (0, 0))
    window.blit(player.get_sprite(), (player.get_coord().get_x() * 30, player.get_coord().get_y() * 30))
    window.blit(exit.get_sprite(), (exit.get_coord().get_x() * 30, exit.get_coord().get_y() * 30))

    for square in grid:
        if square.get_is_wall() is True:
            window.blit(wall, (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))

        else:
            if square.get_has_item() is True:
                window.blit(square.get_item().get_sprite(), (square.get_coord().get_x() * 30, square.get_coord().get_y() * 30))
    pygame.display.flip()


def put_item_in_grid(grid, item, player, exit):
    """Method to put the items in the grid, at random positions."""
    for square in grid:
        if square.get_coord().get_x() == item.get_coord().get_x() and square.get_coord().get_y() == item.get_coord().get_y():
            if (item.get_coord().get_x() != exit.get_coord().get_x() and item.get_coord().get_y() != exit.get_coord().get_y()) and (item.get_coord().get_x() != player.get_coord().get_x() and item.get_coord().get_y() != player.get_coord().get_y()):
                if square.get_has_item() is True:
                    item.set_coord(generate_random_coordinates())
                    put_item_in_grid(grid, item, player, exit)
                    break
                if square.get_is_wall() is True:
                    item.set_coord(generate_random_coordinates())
                    put_item_in_grid(grid, item, player, exit)
                    break
                if square.get_is_wall() is False and square.get_has_item() is False:
                    square.set_has_item(True)
                    square.set_item(item)
                    break
            else:
                item.set_coord(generate_random_coordinates())
                put_item_in_grid(grid, item, player, exit)
                break

    return grid
