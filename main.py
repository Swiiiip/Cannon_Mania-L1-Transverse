# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#imports
import math
import pygame
from objects import Enemy, Bullet
import random

#initialize pygame
pygame.init()

#initialize pygame mixer for the music
pygame.mixer.init()

 #initialize the window
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

FPS = 60

   
#initialize images (canon (divided in the shooting part and the stand), the sky and the ground)
canon_shoot = pygame.transform.smoothscale(pygame.image.load("cannon.png").convert_alpha(), (130, 47))
canon_stand_image = pygame.transform.smoothscale(pygame.image.load("cannon2.png").convert_alpha(),(66,48))

background_sky = pygame.transform.smoothscale(pygame.image.load("sky.jpg").convert_alpha(),(1200,670))

background_grass = pygame.transform.smoothscale(pygame.image.load("ground.png").convert_alpha(),(64,64))

background_ground = pygame.transform.smoothscale(pygame.image.load("ground_2.png").convert_alpha(),(63,44))

start_button = pygame.transform.smoothscale(pygame.image.load("start_button.png").convert_alpha(), (200, 114))

exit_button = pygame.transform.smoothscale(pygame.image.load("Exit_button.png").convert_alpha(), (200, 85) )

castle_start = pygame.transform.smoothscale(pygame.image.load("castle_start.png").convert_alpha(), (700, 454))

#For the collision of enemies with the canon 
canon_stand = canon_stand_image.get_rect()
player_rect = canon_shoot.get_rect(center=(215, 625))

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 0


def start_menu():

    run = True
    while run:
        # Sky Background (Actually drawing it)
        window.fill((255, 255, 255))
        window.blit(background_sky, (0, 0))


        # Loop to draw the grass because the size of it is small, so we draw it multiple times on the same y, but changing the x
        for x in range(0,1200,64):
            window.blit(background_grass,(x,660))
        
        # Loop to draw the ground because the size of it is small, so we draw it multiple times on tdifferent y's and x's
        for y in range(64,800,43):
            for x in range(0, 1200, 63):
                window.blit(background_ground, (x, 660 + y))
        
        window.blit(start_button, (window_width/2 - 110, 200))
        window.blit(exit_button, (window_width/2- 110, 300))
        window.blit(castle_start, (window_width/2 - 350, 210))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        
        pygame.display.flip()
               
                

def game_function():

    
    #correction_angle = 0

    #initialize the objects
    bullets = []
    enemies = []



    #Enemies spawning probability
    ENEMY_SPAWN_PROBABILITY_PER_SECOND = 0.5
    SPAWN_COOLDOWN = 200
    enemy_spawn_cooldown = False
    enemy_spawn_cooldown_counter = 0
    enemy_spawn_probability = ENEMY_SPAWN_PROBABILITY_PER_SECOND / FPS
    #Life bar
    max_life = 100
    life = max_life

    

    clock = pygame.time.Clock()

    run = True
    while run:



        pygame.mouse.set_visible(False)#Make the mouse invisible

        


        
        
        # Sky Background (Actually drawing it)
        window.fill((255, 255, 255))
        window.blit(background_sky, (0, 0))


        # Loop to draw the grass because the size of it is small, so we draw it multiple times on the same y, but changing the x
        for x in range(0,1200,64):
            window.blit(background_grass,(x,660))
        
        # Loop to draw the ground because the size of it is small, so we draw it multiple times on tdifferent y's and x's
        for y in range(64,800,43):
            for x in range(0, 1200, 63):
                window.blit(background_ground, (x, 660 + y))
        


        mx, my = pygame.mouse.get_pos() #Positions of the mouse

        #Half of the window size

        if my > 620: 
            my = 620
        if mx < 200:
            mx = 200
        
        #Rotation of the canon
        dx, dy = mx - player_rect.centerx, my - player_rect.centery 
        angle = math.degrees(math.atan2(-dy, dx)) - correction_angle
        canon = pygame.transform.rotate(canon_shoot, angle)
        rot_image_rect = canon.get_rect(center=(215, 625))

        window.blit(canon, rot_image_rect)
        window.blit(canon_stand_image,(165,615))

    
    
        # display life
        pygame.draw.rect(window, (100, 0, 0), (10, 100, max_life, 10))
        pygame.draw.rect(window, (255, 0, 0), (10, 100, life, 10))

        if not enemy_spawn_cooldown:
            if random.random() < enemy_spawn_probability:
                enemy_spawn_cooldown = True
                '''enemies.append(EnemyFalling(ARROW, game))
                enemies.append(EnemyFalling(ARROW, game))
                enemies.append(EnemyFalling(ARROW, game))
                enemies.append(EnemyFalling(ARROW, game))
                if random.random() < 0.5:
                    enemies.append(Cat(game))
                else:
                    enemies.append(Rock(game))'''
                width = random.randint(100, 200)
                height = random.randint(100, 200)

                ypos = (window.get_height() - 140 - height) if random.random() < 0.5 else 200


                enemies.append(Enemy(random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)]), window.get_width() + width, ypos, width, height, 5))

        # Spawn cooldown
        else:
            enemy_spawn_cooldown_counter += clock.get_time()
            if enemy_spawn_cooldown_counter >= SPAWN_COOLDOWN:
                enemy_spawn_cooldown = False
                enemy_spawn_cooldown_counter = 0

        for enemy in enemies:
            enemy.move()
            if (rot_image_rect.colliderect(enemy.rect) or enemy.rect.x <= -enemy.rect.width):
                enemies.remove(enemy)
                life -= 10
            
            else:
                enemy.draw(window)

        if life <= 0:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y <= 600 and len(bullets) < 1:
                    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    b = Bullet((0,0,0), 200, 620, 20, 20, 20, x, y)
                    #b.draw(window,color)
                    bullets.append((b,color))
                    #pygame.mixer.sound.play()

        for b in bullets:
            b[0].move()

            found = False
            for enemy in enemies:
                if enemy.collide_with(b[0]):
                    bullets.remove(b)
                    enemies.remove(enemy)
                    found = True


            if not found and (b[0].x > window.get_width() or b[0].x < 0 or b[0].y > window.get_height()):
                bullets.remove(b)

            b[0].draw(window,b[1])


        pygame.display.flip()
        clock.tick(FPS)

    


    '''

    enemy_spawn_cooldown = False
    enemy_spawn_cooldown_counter = 0
    enemy_spawn_cooldown = SPAWN_PROBABILITY_PER_SECOND / FPS

    for obstacle in enemies:
        obstacle.update()

    for projectile in game.projectiles:
        projectile.update()
        for obstacle in enemies:
            if isinstance(obstacle, EnemyFalling) and projectile.rect.colliderect(obstacle.rect):
                enemies.remove(obstacle)
                game.projectiles.remove(projectile)

    if not enemy_spawn_cooldown:
        if random.random() < enemy_spawn_cooldown:
            enemy_spawn_cooldown = True
            enemies.append(EnemyFalling(ARROW, game))
            enemies.append(EnemyFalling(ARROW, game))
            enemies.append(EnemyFalling(ARROW, game))
            enemies.append(EnemyFalling(ARROW, game))
            if random.random() < 0.5:
                enemies.append(Cat(game))
            else:
                enemies.append(Rock(game))

    # Spawn cooldown
    else:
        enemy_spawn_cooldown_counter += clock.get_time()
        if enemy_spawn_cooldown_counter >= SPAWN_COOLDOWN:
            enemy_spawn_cooldown = False
            enemy_spawn_cooldown_counter = 0

    # Apply obstacles
        for obstacle in enemies:
            screen.blit(obstacle.image, obstacle.rect)

    '''

    pygame.quit()
    exit()
start_menu()
game_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
