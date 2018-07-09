import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement of the flag"""
        # Update the ship's center value, not the rect
        if self.moving_right == True:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left == True:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at each current location"""
        self.screen.blit(self.image, self.rect)
