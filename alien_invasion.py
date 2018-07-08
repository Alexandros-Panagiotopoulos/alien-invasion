import sys

import pygame

def run_game():
    #initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien_Invasion")
    #set the backgraound color
    bg_color = (230, 230, 230)
    #start the main loop for the game
    while True:

        #Watch the mouse and keypboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
