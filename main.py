# This is a sample Python script.
import pygame
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import math
import pygame
from objects import *

pygame.init()
window = pygame.display.set_mode((1200, 800))
canon_shoot = pygame.transform.smoothscale(pygame.image.load("cannon.png").convert_alpha(), (130, 47))
canon_stand_image = pygame.transform.smoothscale(pygame.image.load("cannon2.png").convert_alpha(),(66,48))

background_sky = pygame.transform.smoothscale(pygame.image.load("v1015-101a.jpg").convert_alpha(),(1200,670))
background_grass = pygame.transform.smoothscale(pygame.image.load("ground.png").convert_alpha(),(64,64))
background_ground = pygame.transform.smoothscale(pygame.image.load("ground_2.png").convert_alpha(),(63,44))

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 0






bullets = []
enemies = []

sq = Square((0,255,0),200,200,100,100, 10) #Bullets

run = True
while run:

    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # print(x,y)
            b = Bullet((255,0,0), sq.rect.centerx, sq.rect.centery, 20, 20, 20, x, y)
            bullets.append(b)

    for b in bullets:
        b.move()
    for e in enemies:
        e.move()




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

    for b in bullets:
        b.draw(window)
    for e in enemies:
        e.draw(window)


    pygame.display.flip()




pygame.quit()
exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
