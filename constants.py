import pygame
from pathlib import Path

#initialize pygame
pygame.init()

#initialize the window
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

FPS = 60

# Import images :

# Background :
background_sky = pygame.transform.smoothscale(pygame.image.load("textures/sky.jpg").convert_alpha(),(1200,670))
background_grass = pygame.transform.smoothscale(pygame.image.load("textures/ground.png").convert_alpha(),(64,64))
background_ground = pygame.transform.smoothscale(pygame.image.load("textures/ground_2.png").convert_alpha(),(63,44))

# Texts :
game_title = pygame.transform.smoothscale(pygame.image.load("textures/game_title.png").convert_alpha(), (700, 67))
health_bar = pygame.transform.smoothscale(pygame.image.load("textures/health_bar.png").convert_alpha(),(200,39))

# Buttons :
start_button_before_hover = pygame.transform.smoothscale(pygame.image.load("textures/start_button_before_hover.png").convert_alpha(), (200, 114))
start_button = pygame.transform.smoothscale(pygame.image.load("textures/start_button.png").convert_alpha(), (200, 114))

exit_button = pygame.transform.smoothscale(pygame.image.load("textures/Exit_button.png").convert_alpha(), (200, 85) )
exit_button_before_hover = pygame.transform.smoothscale(pygame.image.load("textures/Exit_button_before_hover.png").convert_alpha(), (200, 85) )

play_again_button = pygame.transform.smoothscale(pygame.image.load("textures/play_again_button.png").convert_alpha(), (200, 85) )
play_again_button_before_hover =  pygame.transform.smoothscale(pygame.image.load("textures/play_again_button_before_hover.png").convert_alpha(), (200, 85) )

# Castles :
tower = pygame.transform.smoothscale(pygame.image.load("textures/Tower.png").convert_alpha(),(230,550))

castle_start = pygame.transform.smoothscale(pygame.image.load("textures/castle_start.png").convert_alpha(), (700, 454))
castle_end = pygame.transform.smoothscale(pygame.image.load("textures/Castle_end.png").convert_alpha(), (700,454))

# Cannon :
cannon_shoot = pygame.transform.smoothscale(pygame.image.load("textures/cannon.png").convert_alpha(), (200, 57))
cannon_stand = pygame.transform.smoothscale(pygame.image.load("textures/cannon2.png").convert_alpha(), (66, 48))

# CannonBall :
cannon_ball = pygame.transform.smoothscale(pygame.image.load("textures/cannon_ball.png").convert_alpha(), (40, 40))

# Enemies :
plane = pygame.transform.smoothscale(pygame.image.load("textures/plane.png").convert_alpha(), (150, 75))
ground_enemy1 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy1.png").convert_alpha(), (150, 200))
ground_enemy2 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy2.png").convert_alpha(), (100, 100))
ground_enemy3 = pygame.transform.smoothscale(pygame.image.load("textures/ground_enemy3.png").convert_alpha(), (100, 125))

enemyList = { 0:(plane, 2) , 1:(ground_enemy1,3) , 2:(ground_enemy2,4) , 3:(ground_enemy3,5) } # enemyList[i] = (images, speed)

# Explosion effects :
explosionFrames = []
for frame in Path("/textures/explosion").glob("*.jpg"):
    explosionFrames.append( pygame.transform.smoothscale(pygame.image.load(frame).convert_alpha(), (128, 80)) )

for frame in explosionFrames:
    print(frame)


# Initialize and load music and sounds

#Background music :
background_music_start = pygame.mixer.Sound('audio/Wii Music - No Copyright.mp3')
background_music_start.set_volume(0.3)
background_music_game = pygame.mixer.Sound("audio/music.mp3")

#Game sounds :
cannon_shot_sound = pygame.mixer.Sound('audio/Cannon Sound Effect.mp3')
cannon_shot_sound.set_volume(0.1)
mouse_click_sound = pygame.mixer.Sound('audio/Mouse Click Sound Effect (No Copyright).mp3')
score_sound = pygame.mixer.Sound('audio/Score.mp3')


#AUGH_sound = pygame.mixer.Sound('audio/AUGHHHH sound effect tiktok snoring meme.mp3')


#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down

