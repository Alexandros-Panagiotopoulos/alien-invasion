import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    #Make a ship
    ship = Ship(screen)

    #start the main loop for the game
    while True:

        #Watch the mouse and keypboard events.
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
