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

down = True
objects = []
while done is not True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            objects.append([x, y])

    screen.fill(BLACK)

    

    for i, coords in enumerate(objects):
        pygame.draw.line(screen, WHITE, coords, [coords[0], coords[1]+10], 2)

        if y-10 > 0:

            objects[i][1] -= y_change

    pygame.display.flip()

    
    # screen.fill(WHITE)
    # pygame.display.flip()

    clock.tick(60)

pygame.quit()