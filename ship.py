import pygame

class Ship():

    def __init__(self, screen):
        """initialize the ship and set its starting position"""
        self.screen = screen

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement of the flag"""
        if self.moving_right == True:
            self.rect.centerx += 1.5
        elif self.moving_left == True:
            self.rect.centerx -= 1.5

    def blitme(self):
        """draw the ship at each current location"""
        self.screen.blit(self.image, self.rect)
