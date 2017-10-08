# 3rd party modules
import pygame
import libtcodpy as libtcod

# game files
import constants

 # ________  _________  ________  ___  ___  ________ _________
# |\   ____\|\___   ___\\   __  \|\  \|\  \|\   ____\\___   ___\
# \ \  \___|\|___ \  \_\ \  \|\  \ \  \\\  \ \  \___\|___ \  \_|
 # \ \_____  \   \ \  \ \ \   _  _\ \  \\\  \ \  \       \ \  \
  # \|____|\  \   \ \  \ \ \  \\  \\ \  \\\  \ \  \____   \ \  \
    # ____\_\  \   \ \__\ \ \__\\ _\\ \_______\ \_______\  \ \__\
   # |\_________\   \|__|  \|__|\|__|\|_______|\|_______|   \|__|
   # \|_________|

class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path
# if tile is False player can walk over it.
# if tile is True player can NOT walk over it.


  # ______   .______          __   _______   ______ .___________.    _______.
 # /  __  \  |   _  \        |  | |   ____| /      ||           |   /       |
# |  |  |  | |  |_)  |       |  | |  |__   |  ,----'`---|  |----`  |   (----`
# |  |  |  | |   _  <  .--.  |  | |   __|  |  |         |  |        \   \
# |  `--'  | |  |_)  | |  `--'  | |  |____ |  `----.    |  |    .----)   |
 # \______/  |______/   \______/  |_______| \______|    |__|    |_______/
class obj_Actor:
    """Our basic actor object."""

    def __init__(self, x, y, sprite):
        """Create the actor and set its coordinates."""
        self.x = x  # map address (not a pixel address)
        self.y = y  # map address (not a pixel address)
        self.sprite = sprite

    def draw(self):
        """Have the actor draw itself."""
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.CELL_WIDTH,
                                        self.y*constants.CELL_HEIGHT))

    def move(self, dx, dy):
        """Move the actor.

        dx = distance to move x.  dy = distance to move y.
        The actor checks where it and where he wants to move to.
        Decides if where he wants to move to is a floor tile or a wall tile.
        """
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy

# .___  ___.      ___      .______
# |   \/   |     /   \     |   _  \
# |  \  /  |    /  ^  \    |  |_)  |
# |  |\/|  |   /  /_\  \   |   ___/
# |  |  |  |  /  _____  \  |  |

def map_create():
    new_map = [[struc_Tile(False) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]


    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map

 # .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |  ________    | || |  _______     | || |      __      | || | _____  _____ | || |     _____    | || | ____  _____  | || |    ______    | |
# | | |_   ___ `.  | || | |_   __ \    | || |     /  \     | || ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | |
# | |   | |   `. \ | || |   | |__) |   | || |    / /\ \    | || |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | |
# | |   | |    | | | || |   |  __ /    | || |   / ____ \   | || |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || | | |    ____  | |
# | |  _| |___.' / | || |  _| |  \ \_  | || | _/ /    \ \_ | || |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | |
# | | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | |
# | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |

def draw_game():
   # _____          __  __ ______
  # / ____|   /\   |  \/  |  ____|
 # | |  __   /  \  | \  / | |__
 # | | |_ | / /\ \ | |\/| |  __|
 # | |__| |/ ____ \| |  | | |____


    global SURFACE_MAIN

    # clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # draw the map
    draw_map(GAME_MAP)

    #draw the character
    PLAYER.draw()

    # update the display
    pygame.display.flip()

def draw_map(map_to_draw):
    # The following could be done as a list comprehension but it would be ugly
    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True: # if True there is a wall here
                #draw wall
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))
            else:
                #draw floor
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.CELL_WIDTH, y*constants.CELL_HEIGHT))

def game_main_loop():
    """In this function we loop the main game."""
    game_quit = False

    while not game_quit:

        # get player input
        events_list = pygame.event.get()

        #process input
        for event in events_list:  # loop through all events that have happened
            if event.type == pygame.QUIT:  # QUIT attribute - someone closed window
                game_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0, 1)
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1, 0)
         #draw the game
        draw_game()

    pygame.quit()
    exit()

def game_initialize():
    """This function initializes the main window, and pygame"""

    global SURFACE_MAIN, GAME_MAP, PLAYER
    # initialize pygame
    pygame.init()

    # set sufrace dimensions
    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))
    # Ideally the surface should be resizable -- we are going to skip this for now

    GAME_MAP = map_create() # Create the game map. Fills the 2D array with values.

    PLAYER = obj_Actor(0, 0, constants.S_PLAYER)

    ENEMY = obj_Actor(10, 10, constants.S_ENEMY)

 # .     *        .    *       ________________ _      .    ____      *
     # *     .       .     .  <-_______________|*) .  ___==/    \==___
                     # . *     ~.      *   | |  ~  --==================--
   # .    *     *                 .      . | |  *  /  ^/  --=====--
    # .     .     .         .        ______|_|____/___/     .        .
  # .   *  .       *   .      ()   . ==__        ....^T/_      .
      # .      .      .*      .    .  *  --___________|\~  .     *.    .
  # .              .        .   *    .            .        *     .

#
          # ____                                 ,--.
        # ,'  , `.   ,---,         ,---,       ,--.'|
     # ,-+-,.' _ |  '  .' \     ,`--.' |   ,--,:  : |
  # ,-+-. ;   , || /  ;    '.   |   :  :,`--.'`|  ' :
 # ,--.'|'   |  ;|:  :       \  :   |  '|   :  :  | |
# |   |  ,', |  '::  |   /\   \ |   :  |:   |   \ | :
# |   | /  | |  |||  :  ' ;.   :'   '  ;|   : '  '; |
# '   | :  | :  |,|  |  ;/  \   \   |  |'   ' ;.    ;
# ;   . |  ; |--' '  :  | \  \ ,'   :  ;|   | | \   |
# |   : |  | ,    |  |  '  '--' |   |  ''   : |  ; .'
# |   : '  |/     |  :  :       '   :  ||   | '`--'
# ;   | |`-'      |  | ,'       ;   |.' '   : |
# |   ;/          `--''         '---'   ;   |.'
# '---'                                 '---'

if __name__ == '__main__':
    game_initialize()
    game_main_loop()
