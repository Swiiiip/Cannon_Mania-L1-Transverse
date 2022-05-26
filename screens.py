import random
from objects import *
from constants import *

#initialize pygame mixer for the music
pygame.mixer.init()

# Function used in each menu in order to display the basic back_ground(Sky, grass and dirt)
def display_background():

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


#Function of the screen at the beggining (before playing)
def start_menu():
    run = True
    background_music_start.play()

    while run:
        display_background()

        window.blit(start_button_before_hover, (window_width / 2 - 110, 200))
        window.blit(exit_button_before_hover, (window_width / 2 - 110, 300))
        window.blit(castle_start, (window_width / 2 - 350, 210))

        window.blit(game_title, (window_width/2 - 350, 80))

        mx, my = pygame.mouse.get_pos()  # Positions of the mouse

        if (mx > window_width / 2 - 95 and mx < window_width / 2 - 135 + 200 and my > 210 and my < 290):
            window.blit(start_button, (window_width / 2 - 110, 200))

        if (mx > window_width / 2 - 90 and mx < window_width / 2 - 138 + 200 and my > 310 and my < 370):
            window.blit(exit_button, (window_width / 2 - 110, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button is pressed
                if(mx > window_width/2 - 95 and mx < window_width/2 - 135 + 200 and my > 210 and my < 290):# borders of the start button, so basically if he start button has been pressed
                    mouse_click_sound.play() # click sound
                    game_function() # go to the game

                if(mx > window_width/2 - 90 and mx < window_width/2 - 138 + 200 and my > 310 and my < 370):# borders of the start button, so basically if he start button has been pressed
                    mouse_click_sound.play()# click sound
                    pygame.quit() # quit the game

        pygame.display.flip()

# Function for the screen after losing
def End_menu():
    run = True
    while run:

        pygame.mouse.set_visible(True)  # Make the mouse invisible

        display_background()

        #Display buttons
        window.blit(play_again_button_before_hover, (window_width / 2 + 150, 100))
        window.blit(exit_button_before_hover, (window_width / 2 - 348, 100))

        window.blit(castle_end, (window_width / 2 - 350, 210))

        mx, my = pygame.mouse.get_pos()  # Positions of the mouse

        #Hover detect cursor when on button
        if (mx > window_width / 2 + 150 and mx < window_width / 2 + 350 and my > 100 and my < 185):
            window.blit(play_again_button, (window_width / 2 + 150, 100))

        if (mx > window_width / 2 - 348 and mx < window_width / 2 - 348 + 200 and my > 100 and my < 185):
            window.blit(exit_button, (window_width / 2 - 348, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if(mx > window_width/2 + 150  and mx < window_width/2 + 350 and my > 100 and my < 185): # borders of the play again button, so basically if the play button has been pressed
                    mouse_click_sound.play() #click sound
                    game_function() # go to the game

                if(mx > window_width/2 - 348 and mx < window_width/2 - 348 + 200 and my > 100 and my < 185): ## borders of the exit button, so basically if the exit button has been pressed
                    mouse_click_sound.play()# click sound
                    pygame.quit()# go to the game

        pygame.display.flip()


# Function for the game its self
def game_function():
    background_music_start.stop()
    background_music_game.play()
    background_music_game.set_volume(1)

    #initialize the objects
    bullets = []
    enemies = []

    #Enemies spawning probability
    ENEMY_SPAWN_PROBABILITY_PER_SECOND = 0.5
    SPAWN_COOLDOWN = 20
    enemy_spawn_cooldown = False
    enemy_spawn_cooldown_counter = 0
    enemy_spawn_probability = ENEMY_SPAWN_PROBABILITY_PER_SECOND / FPS

    #Life bar
    max_life = 100
    life = max_life

    #Score text init
    score = 0
    score_font = pygame.font.SysFont("stencil",48) #pygame.font.get_fonts() to see all available fonts
    display_score = score_font.render("Score : "+str(score),True,(0,0,0))

    clock = pygame.time.Clock()

    cannonX, cannonY = 180,615
    cannon = Cannon( cannonX, cannonY ,window)

    run = True
    while run:

        pygame.mouse.set_visible(False)#Make the mouse invisible

        display_background()

        cannon.update()

        tower_rect = tower.get_rect(center = (-10,300))
        window.blit(tower, (-115,113))

        # display health
        window.blit(health_bar, (10, 55))
        pygame.draw.rect(window, (100, 0, 0), (62, 77, max_life+44, 14))
        pygame.draw.rect(window, (255, 0, 0), (62, 77, life+44, 14))

        # display score
        window.blit(display_score, (950, 55))

        if not enemy_spawn_cooldown:
            if random.random() < enemy_spawn_probability:
                enemy_spawn_cooldown = True

                if random.random() < 0.5 : #planes
                    enemy_type = 0

                else : #ground enemies
                    enemy_type = random.randint(1, 3)

                enemies.append( Enemy(enemy_type, window) )

        # Spawn cooldown
        else:
            enemy_spawn_cooldown_counter += clock.get_time()
            if enemy_spawn_cooldown_counter >= SPAWN_COOLDOWN:
                enemy_spawn_cooldown = False
                enemy_spawn_cooldown_counter = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if y <= 600 and x > 180 and len(bullets) < 1:
                    cannon_shot_sound.play()

                    b = Bullet(200, 620, 20, window)
                    bullets.append(b)

        # Move and display bullets and enemies :
        for enemy in enemies:
            enemy.update()
        for b in bullets:
            b.update()

        # Collision detections :
        for enemy in enemies:
            for b in bullets:

                if (b in bullets):

                    if enemy.collide_with(b.bullet_rect): # checks collision enemy and bullet
                        bullets.remove(b)
                        enemies.remove(enemy)

                        score = score + 1
                        if score % 10 == 0:
                            score_sound.set_volume(0.2)
                            score_sound.play()

                        display_score = score_font.render("Score : " + str(score), True, (0, 0, 0))
                        enemy_spawn_probability = enemy_spawn_probability + 0.0004

                    elif (b.x > window.get_width() or b.x < 0) or (b.y > window.get_height() - 158):  # bullet touches ground or sides of screen
                        bullets.remove(b)

            if (enemy in enemies) and (enemy.collide_with(cannon.cannon_rect) or enemy.collide_with(tower_rect)): #enemy hits tower or cannon
                # AUGH_sound.play()
                enemies.remove(enemy)
                life -= 10

                if life <= 0:
                    run = False
                    End_menu()



        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()
    exit()
