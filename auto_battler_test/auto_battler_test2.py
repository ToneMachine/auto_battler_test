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
x_axis_move = 0

def sky(x,y):
    sky_rect = sky_surface.get_rect(topleft = (x,y))
    screen.blit(sky_surface,(sky_rect))

# player/bird
bird = pygame.image.load('auto_battler_test/graphics/bird.png')

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # player inout
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_axis_move -= 5
            elif event.key == pygame.K_d:
                x_axis_move -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                x_axis_move = 0  

    x_axis +=   x_axis_move

    # sky/background surface
    if x_axis <= -960:
        x_axis = 0
    sky(x_axis,y_axis)

    # player/bird
    screen.blit(bird,(0,400))

    # refesh rate
    pygame.display.update()
    clock.tick(60)