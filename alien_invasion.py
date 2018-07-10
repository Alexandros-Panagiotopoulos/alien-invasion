import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    #Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    # Make an alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the main loop for the game
    while True:

        #Watch the mouse and keypboard events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
