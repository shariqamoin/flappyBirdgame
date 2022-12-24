import pygame
import random

# from pygame.constants import KEYDOWN, K_SPACE

#initialising the module in pygame
pygame.init()

#background image load and define co-ordinates
SCREEN = pygame.display.set_mode((500, 750)) 
BACKGROUND_IMAGE = pygame.image.load('background.jpg')

#bird image load and define co-ordinates
BIRD_IMAGE = pygame.image.load('bird.png')
bird_x = 50
bird_y = 350
bird_y_change = 0

#start screen
startfont = pygame.font.Font("freesansbold.ttf",38)
def start():
    display = startfont.render(f'PRESS SPACE TO START', True, (225, 225, 225))
    SCREEN.blit(display, (20, 200))
    pygame.display.update()

#game over screen
gameoverfont1 = pygame.font.Font("freesansbold.ttf", 64)
gameoverfont2 = pygame.font.Font("freesansbold.ttf", 32)    
def game_over():
    display = gameoverfont1.render(f'GAME OVER', True, (100, 0, 0))
    SCREEN.blit(display, (40, 300))
    display = gameoverfont2.render(f'SCORE: {score}', True, (225, 225, 225))
    SCREEN.blit(display, (40, 400))
    pygame.display.update()

#def display bird
def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

#obstacles
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 450)
OBSTACLE_COLOR = (200, 250, 100)
OBSTACE_X_CHANGE = -0.15
obstacle_x = 500

#obstacles def
def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 200
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))

#def game over
score = 0
scorefont = pygame.font.Font("freesansbold.ttf", 32)
def score_display(score):
    display = scorefont.render(f'Score:{score}', True, (225, 225, 225))
    SCREEN.blit(display, (10, 10))

#collision detection
def collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, bottom_OBSTACLE_HEIGHT):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= OBSTACLE_HEIGHT or bird_y >= bottom_OBSTACLE_HEIGHT:
            return True
    return False
score = 0

#setting the display
running = True
waiting = True
collision = False

while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    while waiting:
        if collision:
            game_over()
        start()
        #start game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    score = 0
            #quit game
            if event.type == pygame.QUIT:
                waiting = False
                running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #space bar to change y pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 0.3

    #boundary
    bird_y += bird_y_change
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 650:
        bird_y = 650

    #repeat the obstacles 
    obstacle_x += OBSTACE_X_CHANGE
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT+200)
    if collision == True:
        waiting = True
        obstacle_x = 500
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(150, 450)
        score += 1

    #display obstacle, bird, score
    display_obstacle(OBSTACLE_HEIGHT)
    display_bird(bird_x, bird_y)
    score_display(score)

    pygame.display.update()

pygame.quit()
