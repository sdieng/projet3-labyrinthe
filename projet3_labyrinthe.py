"""Pygame, methods.py and classes.py importation."""
import pygame
from pygame.locals import *
from classes import Item, Player, Exit
from methods import generate_grid, put_item_in_grid, display_grid, generate_random_coordinates


# Initialization of pygame
pygame.init()

# Initialization window and graphic library
window = pygame.display.set_mode((450, 450))
background = pygame.image.load('graphics/background.png').convert()
wall = pygame.image.load('graphics/wall.png').convert()
win = pygame.image.load('graphics/win.png').convert()
lose = pygame.image.load('graphics/lose.png').convert()

# Initialization of the player, grid and exit
player = Player()
exit = Exit()
grid = generate_grid(player, exit)

# Item creation and insertion in grid
# Item no.1
needle = Item("Needle", 'graphics/item1.png')
needle.set_coord(generate_random_coordinates())
grid = put_item_in_grid(grid, needle, player, exit)

# Item no.2
ether = Item("Ether", 'graphics/item2.png')
ether.set_coord(generate_random_coordinates())
grid = put_item_in_grid(grid, ether, player, exit)

# Item no.3
tube = Item("Tube", 'graphics/item3.png')
tube.set_coord(generate_random_coordinates())
grid = put_item_in_grid(grid, tube, player, exit)

# Display of the grid
display_grid(grid, window, wall, background, exit, player)


# Event capture
running = 1
capture = 1
item_count = 0
pygame.key.set_repeat(400, 30)

# 2 loops : one solely for the capture of events, so movements can be disabled when game is over
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

            # Movement by event capture
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    for square in grid:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_y() == (player.get_coord().get_y() + 1) and square.get_coord().get_x() == player.get_coord().get_x() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_grid(grid, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.get_has_item() is True:
                                item_count += 1
                                square.setHasItem(False)
                                square.getItem().setGotItem(True)
                                display_grid(grid, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Checks if the square is the exit, and if it is, checks if the player has all the items
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break

                if event.key == K_UP:
                    for square in grid:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_y() == (player.get_coord().get_y() - 1) and square.get_coord().get_x() == player.get_coord().get_x() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_grid(grid, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.has_item is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_grid(grid, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Checks if the square is the exit, and if it is, checks if the player has all the items
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break

                if event.key == K_LEFT:
                    for square in grid:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_x() == (player.get_coord().get_x() - 1) and square.get_coord().get_y() == player.get_coord().get_y() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_grid(grid, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.get_has_item() is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_grid(grid, window, wall, background, exit, player)
                            pygame.display.flip()
                            # Checks if the square is the exit, and if it is, checks if the player has all the items
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break

                if event.key == K_RIGHT:
                    for square in grid:
                        # Checks if the next square isn't a wall, and sets new coordinates por the player if the condition is true
                        if square.get_coord().get_x() == (player.get_coord().get_x() + 1) and square.get_coord().get_y() == player.get_coord().get_y() and square.get_is_wall() is False:
                            player.set_coord(square.get_coord())
                            display_grid(grid, window, wall, background, exit, player)
                            # Checks if there's an item on the square, and picks it if the condition is true
                            if square.get_has_item() is True:
                                item_count += 1
                                square.set_has_item(False)
                                square.get_item().set_got_item(True)
                                display_grid(grid, window, wall, background, exit, player)
                            pygame.display.flip()
                            if player.get_coord().get_x() == exit.get_coord().get_x() and player.get_coord().get_y() == exit.get_coord().get_y():
                                # Player wins if he has all the items, loses if he misses one, then the game waits for the window to be closed
                                if item_count == 3:
                                    exit.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(win, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                                else:
                                    player.empty()
                                    display_grid(grid, window, wall, background, exit, player)
                                    window.blit(lose, (0, 150))
                                    pygame.display.flip()
                                    capture = 0
                            break
