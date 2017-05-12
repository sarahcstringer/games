import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

done = False
x = size[0]/2.0
y = size[1]

x_change = 0
y_change = 3

objects = []

spaceship_x = size[0]/2.0
spaceship_y = size[1]-15
spaceship_move = 15
spaceship_size = 15

while done is not True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            # quit on escape
            if event.key == pygame.K_ESCAPE:
                done = True

            # shoot if spacebar is hit
            elif event.key == pygame.K_SPACE:
                objects.append([spaceship_x+spaceship_size/2, spaceship_y])

            elif event.key == pygame.K_LEFT and spaceship_x > 0:
                spaceship_x -= spaceship_move

            elif event.key == pygame.K_RIGHT and spaceship_x < size[0]:
                spaceship_x += spaceship_move

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, [spaceship_x, spaceship_y, spaceship_size, spaceship_size])

    for i, coords in enumerate(objects):
        pygame.draw.line(screen, WHITE, coords, [coords[0], coords[1]+10], 2)

        if y-10 > 0:

            objects[i][1] -= y_change

    pygame.display.flip()

    
    # screen.fill(WHITE)
    # pygame.display.flip()

    clock.tick(60)

pygame.quit()