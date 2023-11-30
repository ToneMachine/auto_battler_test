import pygame
from sys import exit

# systems
pygame.init()
screen = pygame.display.set_mode((1920/2, 960))
pygame.display.set_caption("auto battler test")
clock = pygame.time.Clock()

# background surface
sky_surface = pygame.image.load('auto_battler_test/graphics/background.png')
x_axis = 0
y_axis = 0

def sky(x,y):
    sky_rect = sky_surface.get_rect(topleft = (x,y))
    screen.blit(sky_surface,(sky_rect))

# player bird
bird_surface = pygame.image.load('auto_battler_test/graphics/bird.png')
bird_x = 0
bird_y = 480
bird_y_move = 0

def bird(x,y):
    bird_rect = bird_surface.get_rect(midleft = (x,y))
    screen.blit(bird_surface,(bird_rect))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # player inout
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_y_move -= 5
            elif event.key == pygame.K_w:
                bird_y_move -= 5
            
            if event.key == pygame.K_DOWN:
                bird_y_move += 5
            elif event.key == pygame.K_s:
                bird_y_move += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_w or event.key == pygame.K_DOWN or pygame.K_s:
                bird_y_move = 0  

    bird_y += bird_y_move

    # boundaries
    if bird_y <= 79:
        bird_y = 79
    
    elif bird_y >= 893:
        bird_y = 893

    # sky background
    x_axis -= 5
    if x_axis <= -960:
        x_axis = 0
    sky(x_axis,y_axis)

    # player
    bird(bird_x,bird_y)

    # refesh rate
    pygame.display.update()
    clock.tick(60)