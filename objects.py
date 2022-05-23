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
    def __init__(self, color, x, y, width, height, speed, targetx,targety):
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



'''

# class for all the obstacles
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, game):
        super().__init__()

        self.image = image
        self.game = game

        # Rectangle coordinates of the image
        self.rect = self.image.get_rect()

        # The x coordinates of the obstacle to the screen width
        self.rect.x = SCREEN_SIZE[0]
        self.rect.y = START_Y - self.image.get_height()

    def update(self):
        # Move the obstacle across the screen
        self.rect.x -= self.game.speed

        # Remove the obstacle soon as the screen disappear
        if self.rect.x < -self.rect.width:
            self.game.obstacles.pop(self.game.obstacles.index(self))


class EnemyFalling(Enemy):
    def __init__(self, image, game):
        super().__init__(image, game)
        self.rect.x = random.randint(0, SCREEN_SIZE[0])
        self.rect.y = -self.rect.height

        self.volacity_x = random.randint(-10, 10)
        self.volacity_y = 0

    def update(self):
        # Move the obstacle across the screen
        self.rect.x -= self.game.speed + self.volacity_x
        self.rect.y += self.volacity_y
        self.volacity_y += GRAVITY

        # Remove the obstacle soon as the screen disappear
        if self.rect.x < -self.rect.width or self.rect.y > SCREEN_SIZE[1]:
            self.game.obstacles.pop(self.game.obstacles.index(self))


class Cat(Enemy):
    N_CATS = 3
    CATS = [
        pygame.transform.scale(
            sprite, (sprite.get_width() * 2, sprite.get_height() * 2)
        )
        for sprite in [pygame.image.load(f"assets/Cat{i}.png") for i in range(N_CATS)]
    ]

    def __init__(self, obstacles):
        super().__init__(Cat.CATS[random.randrange(Cat.N_CATS)], obstacles)
'''