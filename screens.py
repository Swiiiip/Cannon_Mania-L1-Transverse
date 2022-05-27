# File responsible for game displays (menus, gameplay, background display)

import random
from objects import *
from constants import *

score_font = pygame.font.SysFont("stencil", 48)  # pygame.font.get_fonts() to see all available fonts

global SCORE

#initialize pygame mixer for the music
pygame.mixer.init()



# Function used in each menu in order to display the basic back_ground(Sky, decorations, etc)
def display_background():

        # Sky Background (Actually drawing it)
        window.fill((255, 255, 255))
        window.blit(background_sky, (0, 0))

        # Decorations
        window.blit(background_start, (0,148) )

# Function used in each menu in order to display the ground
def display_ground():

    # Loop to draw the grass because the size of it is small, so we draw it multiple times on the same y, but changing the x
    for x in range(0, 1200, 64):
        window.blit(background_grass, (x, 660))

    # Loop to draw the ground because the size of it is small, so we draw it multiple times on tdifferent y's and x's
    for y in range(64, 800, 43):
        for x in range(0, 1200, 63):
            window.blit(background_ground, (x, 660 + y))


# Function to display the pause menu
def pause_menu():
    run = True
    pygame.mouse.set_visible(True)  # Make the mouse visible

    window.blit(pause_screen, (0,0) )

    button_resume = Button(window_width/2 - resume_button.get_width()/2 , 300 - resume_button.get_height()/2,3)
    button_play_again = Button(window_width/2 - play_again_button.get_width()/2 , button_resume.y + 60 + play_again_button.get_height(),2)
    button_exit = Button(window_width/2 - exit_button.get_width()/2, button_play_again.y + 75 + play_again_button.get_height() ,1)

    while run:

        # Display buttons
        button_resume.update()
        button_play_again.update()
        button_exit.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_resume.isHovered: #clicked resume
                    return True

                if button_play_again.isHovered: #clicked play again
                    game_function()
                    return False

                if button_exit.isHovered: #clicked exit
                    return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # pressed [ESC] again to continue
                    return True

        pygame.display.flip()

#Function of the screen at the beggining (before playing)
def start_menu():

    run = True
    background_music_start.play()

    button_start = Button(window_width/2 - start_button.get_width()/2, 210 ,0)
    button_exit = Button(window_width/2 - exit_button.get_width()/2, 310, 1)

    cannon1 = Cannon(310,615)
    cannon2 = Cannon(820,615)

    while run:

        #Displays :
        display_background()
        window.blit(game_title, (window_width/2 - 350, 80))

        window.blit(castle_start, (window_width / 2 - 350, 210)) #castle
        window.blit(background_start, (0,148) ) # Decorations

        cannon1.update()
        cannon2.update()

        display_ground()

        mx, my = pygame.mouse.get_pos()  # Positions of the mouse

        button_start.update()
        button_exit.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse button is pressed

                if button_start.isHovered : #if mouse is on start button
                    mouse_click_sound.play() # click sound
                    game_function() # go to the game
                    run = False

                if button_exit.isHovered: #if mouse is on exit button
                    mouse_click_sound.play()# click sound
                    pygame.quit() # quit the game

        pygame.display.flip()

# Function for the screen after losing
def end_menu():
    lose_message = score_font.render("You Lost!",True,(0,0,0))
    display_score = score_font.render("Score : " + str(SCORE), True, (0, 0, 0))
    background_music_game.stop()
    background_music_start.play()

    button_play_again = Button(window_width / 2 + 150, 100, 2)
    button_exit = Button(window_width / 2 - 348, 100,1)

    run = True
    while run:

        pygame.mouse.set_visible(True)  # Make the mouse invisible

        display_background()

        # display score
        window.blit(lose_message, (480, 55))
        window.blit(display_score, (475, 115))

        #Display buttons
        button_play_again.update()
        button_exit.update()

        window.blit(castle_end, (window_width / 2 - 350, 110))
        display_ground()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: #checks if player left-clicked

                if button_play_again.isHovered: #checks if mouse is hovering the play again button
                    mouse_click_sound.play() #click sound
                    game_function() # go to the game

                if button_exit.isHovered: #cehcks if mouse is hovering the exit button
                    mouse_click_sound.play()# click sound
                    pygame.quit()# go to the game

        pygame.display.flip()


# Function for the game itself
def game_function():
    global SCORE

    #Background music
    background_music_start.stop()
    background_music_game.play()

    #initialize the objects
    bullets = []
    enemies = []
    explosions = [Explosion(window_width/2,window_height/2,window_width*1.5,window_height*1.5)] #initial explosion for entry transition
    explosion_sound.play()

    #Enemies spawning probability
    ENEMY_SPAWN_PROBABILITY_PER_SECOND = 0.5
    SPAWN_COOLDOWN = 40

    enemy_spawn_cooldown = False
    enemy_spawn_cooldown_counter = 0
    enemy_spawn_probability = ENEMY_SPAWN_PROBABILITY_PER_SECOND / FPS

    shoot_cooldown = False
    shoot_cooldown_counter = 0



    #Life bar
    max_life = 144 # It's the same as 100 but we remove 14,4 144/10 = 14,4
    life = max_life

    #Score text init
    SCORE = 0
    display_score = score_font.render("Score : "+str(SCORE),True,(0,0,0))

    clock = pygame.time.Clock()

    #Initalize cannon
    cannonX, cannonY = 180, 615
    cannon = Cannon( cannonX, cannonY)

    paused = False #displays pause menu when True


    run = True
    while run:
        #life = 0 #instant death
        time = 0

        pygame.mouse.set_visible(False)#Make the mouse invisible

        display_background()
        window.blit(background_game, (1, 118)) # Decorations

        tower_rect = tower.get_rect(center = (-10,300))
        window.blit(tower, (-115,113))

        # display health
        window.blit(health_bar, (10, 55))
        pygame.draw.rect(window, (100, 0, 0), (62, 77, max_life, 14))
        pygame.draw.rect(window, (255, 0, 0), (62, 77, life, 14))

        # display score
        window.blit(display_score, (900, 55))

        #display "[ESC] to Pause"
        window.blit(pause_hint, (900, 85))

        if not enemy_spawn_cooldown:

            if random.random() < enemy_spawn_probability: #random enemy picker
                enemy_spawn_cooldown = True

                random_generator = random.random()

                if random_generator <= 0.15: # 15% chance : planes
                    enemy_type = 0

                elif 0.15 < random_generator <= 0.45: # 30% chance : boulders
                    enemy_type = 1

                elif 0.45 < random_generator <= 0.8:  # 35% chance : 2
                    enemy_type = 2

                else:  # 20% chance : 3
                    enemy_type = 3

                enemies.append( Enemy(enemy_type) ) #stores enemy generated for later display

        # Spawn cooldown
        else:
            enemy_spawn_cooldown_counter += clock.get_time()
            if enemy_spawn_cooldown_counter >= SPAWN_COOLDOWN:
                enemy_spawn_cooldown = False
                enemy_spawn_cooldown_counter = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE: #pause menu
                    paused = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if my <= 625 and mx > 215 and len(bullets) < 1:
                    cannon_shot_sound.play()
                    time += 0.2
                    b = Bullet(200, 620,90, time)
                    bullets.append(b)

        # Move and display objects :

        for enemy in enemies:
            enemy.update()

        for b in bullets:
            b.update()

        cannon.update()

        for explosion in explosions:
            if explosion.frameCount < 9:
                explosion.animate()
            else:
                explosions.remove(explosion)

        display_ground()

        # Collision detections :
        for enemy in enemies:
            for b in bullets:

                if (b in bullets):

                    if enemy.collide_with(b.bullet_rect): # bullet hits enemy
                        bullets.remove(b)
                        explosions.append( Explosion( enemy.x , enemy.enemy_rect.centery  , enemy.enemy_image.get_width(), enemy.enemy_image.get_height() ) )
                        explosion_sound.play()
                        enemies.remove(enemy)

                        SCORE = SCORE + 1
                        if SCORE % 10 == 0:
                            score_sound.set_volume(0.05)
                            score_sound.play()

                        display_score = score_font.render("Score : " + str(SCORE), True, (0, 0, 0))
                        enemy_spawn_probability = enemy_spawn_probability + 0.0004

                    elif (b.x > window.get_width() or b.x < 0) or (b.y > window.get_height() - 158):  # bullet touches ground or sides of screen
                        bullets.remove(b)

            if (enemy in enemies) and (enemy.collide_with(cannon.cannon_rect) or enemy.collide_with(tower_rect)): #enemy hits tower or cannon

                explosions.append( Explosion(enemy.x, enemy.enemy_rect.centery, enemy.enemy_image.get_width(),enemy.enemy_image.get_height()) )
                explosion_sound.play()

                enemies.remove(enemy)

                life -= 14.4*enemy.damage


        if life <= 0:
            run = False
            end_menu()

        if paused:
            paused = False
            background_music_game.set_volume(0.2)
            run = pause_menu()
            background_music_game.set_volume(0.6)

        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()
    exit()
