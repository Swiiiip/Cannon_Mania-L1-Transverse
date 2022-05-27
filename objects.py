# File containing class definitions for sprites (cannon, enemies, cannonBall) and others (buttons, explosion animation)

import math
from constants import *

GRAVITY = 2.5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        data = enemyList[type]
        self.speed = data[1]
        self.damage = data[2]

        self.type = type
        self.rotation = 0

        self.enemy_image = data[0] # image

        self.x = window.get_width() + self.enemy_image.get_width()
        self.y = window.get_height() - self.enemy_image.get_height()/2 - 138
        if type == 0:
            self.y -= 400

        self.enemy_rect = self.enemy_image.get_rect(center=(self.x, self.y)) # hitbox

    def move(self):
        self.x -= self.speed

        if self.type == 1: # checks if boulder
            self.rotation = (self.rotation + self.speed)%360
            self.enemy_image = pygame.transform.rotate(boulder, self.rotation ) #rotate boulder

        self.enemy_rect = self.enemy_image.get_rect(center = ( self.x, self.y )) # update hitbox

    def draw(self):
        window.blit(self.enemy_image,self.enemy_rect)

    def collide_with(self, other_rect):
        # Return True if self collided with other_rect (like the bullet or the cannon)
        return self.enemy_rect.colliderect(other_rect)

    def update(self):
        self.move()
        self.draw()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, time):
        super().__init__()
        mx, my = pygame.mouse.get_pos() #cursor coordinates
        self.x, self.y = x, y # bullet inital position
        self.time = time

        angle = math.atan2(my-y, mx-x) #get angle to target in radians
        self.speed = speed

        self.dx = math.cos(angle)*speed*time
        self.dy = math.sin(angle)*speed*time

        self.rotation = 0 # bullet rotation

        self.bullet_image = cannon_ball # image
        self.bullet_rect = self.bullet_image.get_rect(center = (self.x, self.y)) # hitbox


    def move(self):
        '''
        self.x and self.y are floats (decimals) so I get more accuracy
        if I change self.x and y and then convert to an integer for
        the rectangle.
        '''

        self.dy += (1/2)*GRAVITY*self.time
        
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        self.rotation = ( self.rotation - self.y / (self.speed) ) % 360

        self.bullet_image = pygame.transform.rotate(cannon_ball, self.rotation ) #update image for bullet rotation
        self.bullet_rect = self.bullet_image.get_rect(center = ( int(self.x), int(self.y) )) # update hitbox

    def draw(self):
        window.blit(self.bullet_image,self.bullet_rect)

    def update(self):
        self.move()
        self.draw()


class Cannon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x, self.y = x, y #cannon stand coordinates

        self.cannon_image = cannon_shoot # image
        self.cannon_rect = self.cannon_image.get_rect(center = (self.x+35, self.y+10)) # hitbox

    def rotate(self): #Rotation of the cannon

        mx, my = pygame.mouse.get_pos() #cursor coordinates

        dx, dy = mx - self.cannon_rect.centerx, my - self.cannon_rect.centery #distance between the cursor and the cannon
        angle = math.degrees(math.atan2(-dy, dx)) #angle of the cannon

        self.cannon_image = pygame.transform.rotate(cannon_shoot, angle) #update image
        self.cannon_rect = self.cannon_image.get_rect(center = (self.x+35, self.y+10)) #update hitbox

        # To restrict certain cannon rotations later on
        if angle > 90 :
            angle = 90
        elif angle < 0 and angle > -90 :
            angle = 0
        elif angle <= -90 :
            angle = -90 - angle

    def draw(self):
        window.blit(self.cannon_image, self.cannon_rect )
        window.blit(cannon_stand,(self.x,self.y))

    def update(self):
        self.rotate()
        self.draw()


class Explosion():
    def __init__(self,x,y,width,height):
        self.x, self.y = x, y #position of explosion
        self.w, self.h = width, height #enemy dimensions
        self.frameCount = 0

        self.size = (178 + max( [height,width] ) // 2, 210 + max( [height,width] ) // 2) #size of explosion

        self.explosion_image = explosionFrames[0]

    def animate(self):
        self.frameCount += 0.5

        self.explosion_image = pygame.transform.scale( explosionFrames[ int(self.frameCount) ], self.size )
        self.explosion_rect = self.explosion_image.get_rect(center=(self.x, self.y ))

        window.blit(self.explosion_image, self.explosion_rect )

class Button():
    def __init__(self, x, y, buttonNb):
        self.onImage, self.offImage = buttonList[buttonNb] #on and off images for buttons

        self.x, self.y = x, y #coordinates of button
        self.w, self.h = self.onImage.get_width(), self.onImage.get_height() #size of button

        self.isHovered = False #True when the mouse hovers over the button

    def detect(self):
        mx, my = pygame.mouse.get_pos()  # coordinates of the cursor

        if self.x < mx < self.x + self.w and self.h + self.y > my > self.y : #checks if cursor is within the button box
            self.isHovered = True
        else :
            self.isHovered = False

    def draw(self):
        if self.isHovered:
            window.blit(self.onImage, (self.x,self.y) )
        else:
            window.blit(self.offImage, (self.x,self.y) )

    def update(self):
        self.detect()
        self.draw()
