import pygame
import math
from random import *

class Enemy:
    def __init__(self, color, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed

    def collide_with(self, other_rect):
        # Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


GRAVITY = 0.3

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, targetx,targety):
        super().__init__()
        
        self.rect = pygame.Rect(x, y, width, height)
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians

        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y


    #Override
    def move(self):
        #self.x and self.y are floats (decimals) so I get more accuracy
        #if I change self.x and y and then convert to an integer for
        #the rectangle.
        self.dy += GRAVITY
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self,win,color):
        pygame.draw.circle(win, color , (self.x,self.y) ,20)



