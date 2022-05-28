# File containing images, sounds and other permanent/constant values


import pygame

#initialize pygame
pygame.init()
pygame.display.set_caption('! Cannon Mania !')

#initialize the window
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

FPS = 60

# Import images :

# Background :
background_sky = pygame.transform.smoothscale(pygame.image.load("textures/sky.jpg").convert_alpha(),(1200,670))

background_start = pygame.transform.smoothscale(pygame.image.load("textures/start_bg.png").convert_alpha(),(1200,670))
background_game = pygame.transform.smoothscale(pygame.image.load("textures/game_bg.png").convert_alpha(),(1200,670))

background_grass = pygame.transform.smoothscale(pygame.image.load("textures/ground.png").convert_alpha(),(64,64))
background_ground = pygame.transform.smoothscale(pygame.image.load("textures/ground_2.png").convert_alpha(),(63,44))

pause_screen = pygame.transform.smoothscale(pygame.image.load("textures/pause_screen.png").convert_alpha(),(1200,820))
pause_hint = pygame.transform.smoothscale(pygame.image.load("textures/pause_hint.png").convert_alpha(),(220,60))

# Texts :
game_title = pygame.transform.smoothscale(pygame.image.load("textures/game_title.png").convert_alpha(), (700, 67))
health_bar = pygame.transform.smoothscale(pygame.image.load("textures/health_bar.png").convert_alpha(),(200,39))

# Buttons :
start_button = pygame.transform.smoothscale(pygame.image.load("textures/start_button.png").convert_alpha(), (185, 75))
start_button_before_hover = pygame.transform.smoothscale(pygame.image.load("textures/start_button_before_hover.png").convert_alpha(), (185, 75))

exit_button = pygame.transform.smoothscale(pygame.image.load("textures/Exit_button.png").convert_alpha(), (180, 70) )
exit_button_before_hover = pygame.transform.smoothscale(pygame.image.load("textures/Exit_button_before_hover.png").convert_alpha(), (180, 70) )

play_again_button = pygame.transform.smoothscale(pygame.image.load("textures/play_again_button.png").convert_alpha(), (200, 75) )
play_again_button_before_hover =  pygame.transform.smoothscale(pygame.image.load("textures/play_again_button_before_hover.png").convert_alpha(), (200, 75) )

resume_button = pygame.transform.smoothscale(pygame.image.load("textures/resume_button.png").convert_alpha(), (186, 68) )
resume_button_before_hover = pygame.transform.smoothscale(pygame.image.load("textures/resume_button_before_hover.png").convert_alpha(), (186, 68) )

buttonList = {0:(start_button, start_button_before_hover), 1:(exit_button, exit_button_before_hover), 2:(play_again_button, play_again_button_before_hover), 3:(resume_button, resume_button_before_hover)}

# Castles :
tower = pygame.transform.smoothscale(pygame.image.load("textures/Tower.png").convert_alpha(),(230,550))

castle_start = pygame.transform.smoothscale(pygame.image.load("textures/castle_start.png").convert_alpha(), (700, 454))
castle_end = pygame.transform.smoothscale(pygame.image.load("textures/Castle_end.png").convert_alpha(), (700,554))

# Cannon :
cannon_shoot = pygame.transform.smoothscale(pygame.image.load("textures/cannon.png").convert_alpha(), (200, 57))
cannon_stand = pygame.transform.smoothscale(pygame.image.load("textures/cannon2.png").convert_alpha(), (66, 48))

# CannonBall :
cannon_ball = pygame.transform.smoothscale(pygame.image.load("textures/cannon_ball.png").convert_alpha(), (40, 40))

# Enemies :
missile = pygame.transform.smoothscale(pygame.image.load("textures/missile.png").convert_alpha(), (250, 70))
#ground_enemy1 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy1.png").convert_alpha(), (150, 200))
boulder = pygame.transform.smoothscale(pygame.image.load("textures/boulder.png").convert_alpha(), (220, 220))
#ground_enemy2 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy2.png").convert_alpha(), (100, 100))
car = pygame.transform.smoothscale(pygame.image.load("textures/car.png").convert_alpha(), (280, 120))
#ground_enemy3 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy3.png").convert_alpha(), (100, 125))
moto = pygame.transform.smoothscale(pygame.image.load("textures/moto.png").convert_alpha(), (140, 120))


enemyList = {0:(missile, 4, 2) , 1:(boulder, 2, 2) , 2:(car, 4, 1.5) , 3:(moto, 5, 1)} # enemyList[i] = (image, speed, damage)

# Explosion effects :
explosionFrames = []
for frame in range(10):
    explosionFrames.append( pygame.transform.smoothscale(pygame.image.load("textures/explosions/"+str(frame)+".png").convert_alpha(), (178, 210)) )


# Initialize and load music and sounds

#Background music :
background_music_start = pygame.mixer.Sound('audio/Wii Music - No Copyright.mp3')
background_music_start.set_volume(0.3)

background_music_game = pygame.mixer.Sound("audio/music.mp3")
background_music_game.set_volume(0.6)

#Game sounds :
cannon_shot_sound = pygame.mixer.Sound('audio/Cannon Sound Effect.mp3')
cannon_shot_sound.set_volume(0.4)

mouse_click_sound = pygame.mixer.Sound('audio/Mouse Click Sound Effect (No Copyright).mp3')
score_sound = pygame.mixer.Sound('audio/Score.mp3')
cannon_shot_sound.set_volume(0.6)

explosion_sound = pygame.mixer.Sound('audio/Explosion.mp3')
explosion_sound.set_volume(0.4)

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down

