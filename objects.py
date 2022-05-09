import pygame
import math
from random import *

class Square:
    def __init__(self, color, x, y, width, height, speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = 'E'
        self.speed = speed

    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Bullet(Square):
    def __init__(self, color, x, y, width, height, speed, targetx,targety):
        super().__init__(color, x, y, width, height, speed)
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
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self,win,color):
        pygame.draw.circle(win, color , (self.x,self.y) ,20)