import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    # Make the play button
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)
    #Create an instance to store game statistics and create a Scoreboard
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
