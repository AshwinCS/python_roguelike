# 3rd party modules
import pygame
import libtcodpy as libtcod

# game files
import constants

def draw_game():

    global SURFACE_MAIN

    #TODO clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    #TODO draw the map

    #TODO draw the character
    SURFACE_MAIN.blit(constants.S_PLAYER, ( 200, 200 ))
    # Pygame addresses: 0,0 is upper left hand corner
    # x,y coordinates for character are at the upper left hand corner
    # of the sprite

    #TODO update the display
    pygame.display.flip()



def game_main_loop():
    """In this function we loop the main game."""
    game_quit = False

    while not game_quit:

        # get player input
        events_list = pygame.event.get()

        for event in events_list:  # loop through all events that have happened
            if event.type == pygame.QUIT:  # QUIT attribute - someone closed window
                game_quit = True

         #draw the game
        draw_game()

    pygame.quit()
    exit()

def game_initialize():
    """This function initializes the main window, and pygame"""
    global SURFACE_MAIN
    # initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))   # sets sufrace dimensions
    # Ideally the surface should be resizable -- we are going to skip this for now


if __name__ == '__main__':
    game_initialize()
    game_main_loop()
