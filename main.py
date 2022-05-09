# This is a sample Python script.
import pygame
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import math
import pygame
from objects import *
from random import *

pygame.init()

pygame.mixer.init()
#bullet_sent = pygame.mixer.Sound()


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


clock = pygame.time.Clock()


run = True
while run:
    clock.tick(60)
    pygame.mouse.set_visible(True)


    player_rect = canon_shoot.get_rect(center=(585,620))
    canon_stand = canon_stand_image.get_rect()
    mx, my = pygame.mouse.get_pos()

    if my>600: #Half of the window size
        my=600

    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
    canon = pygame.transform.rotate(canon_shoot, angle)
    rot_image_rect = canon.get_rect(center=(585,620))





    # Background
    window.fill((255, 255, 255))
    window.blit(background_sky, (0, 0))

    for x in range(0,1200,64):
        window.blit(background_grass,(x,660))
    for y in range(64,800,43):
        for x in range(0, 1200, 63):
            window.blit(background_ground, (x, 660 + y))

    window.blit(canon_stand_image,(550,615))

    window.blit(canon, rot_image_rect)
    for b in bullets:
        (b[0]).draw(window,b[1])






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (not(y>600)) and len(bullets)<3:
                color = (randint(0,255),randint(0,255),randint(0,255))
                b = Bullet((0,0,0), 570, 620, 20, 20, 20, x, y)
                b.draw(window,color)
                bullets.append((b,color))
                #pygame.mixer.sound.play()

    for b in bullets:
        b[0].move()
        if b[0].x>1200 or b[0].x<0 or b[0].y>800 or b[0].y<0:
            bullets.remove(b)
    window.blit(canon, rot_image_rect)

    pygame.display.flip()




pygame.quit()
exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
