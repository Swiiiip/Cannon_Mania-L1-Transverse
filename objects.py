import math
from constants import *

GRAVITY = 2.5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type, window):
        self.window = window
        data = enemyList[type]
        self.speed = data[1]

        self.enemy_image = data[0] # image

        self.x = window.get_width() + self.enemy_image.get_width()
        self.y = window.get_height() - self.enemy_image.get_height()/2 - 138
        if type == 0:
            self.y -= 400

        self.enemy_rect = self.enemy_image.get_rect(center=(self.x, self.y)) # hitbox

    def move(self):
        self.x -= self.speed

        #self.enemy_image = pygame.transform.rotate(cannon_ball, self.rotation ) #update image
        self.enemy_rect = self.enemy_image.get_rect(center = ( self.x, self.y )) # update hitbox

    def draw(self):
        self.window.blit(self.enemy_image,self.enemy_rect)

    def collide_with(self, other_rect):
        # Return True if self collided with other_rect (like the bullet or the cannon)
        return self.enemy_rect.colliderect(other_rect)

    def update(self):
        self.move()
        self.draw()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, time, window):
        super().__init__()

 
        self.time = time
        self.window = window

        mx, my = pygame.mouse.get_pos() #cursor coordinates
        self.x, self.y = x, y # bullet inital position

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
        self.window.blit(self.bullet_image,self.bullet_rect)

    def update(self):
        self.move()
        self.draw()

class Cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, window):
        self.x, self.y = x, y #cannon stand coordinates
        self.window = window

        self.cannon_image = cannon_shoot # image
        self.cannon_rect = self.cannon_image.get_rect(center = (self.x+35, self.y+10)) # hitbox

    def rotate(self): #Rotation of the cannon

        mx, my = pygame.mouse.get_pos() #cursor coordinates

        
        dx, dy = mx - self.cannon_rect.centerx, my - self.cannon_rect.centery #distance between the cursor and the cannon
        angle = math.degrees(math.atan2(-dy, dx)) #angle of the cannon
        
        # To restrict certain cannon rotations later on
        if angle > 90 :
            angle = 90
        elif angle < 0 and angle > -90 :
            angle = 0
        elif angle <= -90 :
            angle = -90 - angle

        self.cannon_image = pygame.transform.rotate(cannon_shoot, angle) #update image
        self.cannon_rect = self.cannon_image.get_rect(center = (self.x+35, self.y+10)) #update hitbox

    def draw(self):
        self.window.blit(self.cannon_image, self.cannon_rect )
        self.window.blit(cannon_stand,(self.x,self.y))

    def update(self):
        self.rotate()
        self.draw()



