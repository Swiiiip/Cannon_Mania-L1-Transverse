# This is a sample Python script.
import pygame
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import math
import pygame

pygame.init()
window = pygame.display.set_mode((1200, 800))
canon_shoot = pygame.transform.smoothscale(pygame.image.load("cannon.png").convert_alpha(), (150, 67))
canon_stand_image = pygame.transform.smoothscale(pygame.image.load("cannon2.png").convert_alpha(),(86,68))

background_sky = pygame.transform.smoothscale(pygame.image.load("v1015-101a.jpg").convert_alpha(),(1200,670))
background_grass = pygame.transform.smoothscale(pygame.image.load("ground.png").convert_alpha(),(64,64))
background_ground = pygame.transform.smoothscale(pygame.image.load("ground_2.png").convert_alpha(),(63,44))

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


ball = Ball(30,30,100,100,(0,0,255))

ball_group = pygame.sprite.Group()
ball_group.add(ball) #Lists ?

class Bullet(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

bullets_shoot = []

run = True
while run:

    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if len(bullets_shoot) < 5:
                bullets_shoot.append(Bullet(590, 610, 10, (0, 0, 0), 1))

    player_rect = canon_shoot.get_rect(center=(590,610))
    canon_stand = canon_stand_image.get_rect()
    mx, my = pygame.mouse.get_pos()

    if my>600: #Half of the window size
        my=600
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
    canon = pygame.transform.rotate(canon_shoot, angle)
    rot_image_rect = canon.get_rect(center=(590,610))
    window.fill((255, 255, 255))
    window.blit(background_sky,(0,0))

    for x in range(0,1200,64):
        window.blit(background_grass,(x,660))
    for y in range(64,800,43):
        for x in range(0, 1200, 63):
            window.blit(background_ground, (x, 660 + y))


    window.blit(canon, rot_image_rect)
    window.blit(canon_stand_image,(550,600))
    ball_group.draw(window)

    for bullet in bullets_shoot:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
        else:
            bullets_shoot.pop(bullets_shoot.index(bullet))  # This will remove the bullet if it is off the screen

    for bullet in bullets_shoot:
        bullet.draw(window)


    pygame.display.flip()



pygame.quit()
exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
