import pygame

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# mathematical constants
PI = 3.141592653

# screen info
size = (700, 500)

# characters and such
class LaserBeam(pygame.sprite.Sprite):
    """LaserBeam class."""

    def __init__(self, x, y):
        super(LaserBeam, self).__init__()
        self.image = pygame.Surface([2, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spaceship(pygame.sprite.Sprite):
    """Spaceship -- should only be one per game."""

    def __init__(self):
        super(Spaceship, self).__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = size[0]/2.0
        self.rect.y = size[1]-15

class Blob(pygame.sprite.Sprite):
    """Blobs."""

    def __init__(self, x, y, size=40):
        super(Blob, self).__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = size
        self.direction = 'right'

    def move(self):
        """Move right and left across screen."""
        if self.direction == 'right':
            self.rect.x += 5
            if self.rect.x > size[0]-10:
                self.direction = 'left'
        elif self.direction == 'left':
            self.rect.x -= 5
            if self.rect.x < 0:
                self.direction = 'right'


def main():

    # start the game
    pygame.init()

    # screen settings

    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    pygame.display.set_caption('Game')

    clock = pygame.time.Clock()

    done = False

    lasers = pygame.sprite.Group()
    spaceships = pygame.sprite.Group()
    player = Spaceship()
    spaceships.add(player)

    blobs = pygame.sprite.Group()
    blob = Blob(350, 350)
    blobs.add(blob)

    # main game loop
    while done is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                # quit on escape
                if event.key == pygame.K_ESCAPE:
                    done = True

                elif event.key == pygame.K_SPACE:
                    laser = LaserBeam(player.rect.x+15/2.0, player.rect.y)
                    lasers.add(laser)

                elif event.key == pygame.K_RIGHT:
                    player.rect.x += 15

                elif event.key == pygame.K_LEFT:
                    player.rect.x -= 15


        screen.fill(BLACK)

        for blob in blobs:

            hits = pygame.sprite.spritecollide(blob, lasers, True)
            if hits:
                if blob.size < 25:
                    blobs.remove(blob)
                else:
                    blob1 = Blob(blob.rect.x, blob.rect.y, blob.size *.75)
                    blob2 = Blob(blob.rect.x, blob.rect.y, blob.size *.75)
                    blob2.direction = 'left'

                    blobs.remove(blob)
                    blobs.add(blob1)
                    blobs.add(blob2)

        for thing in blobs:
            thing.move()

        blobs.draw(screen)
        spaceships.draw(screen)

        for laser in lasers:
            laser.rect.y -= 10
            if laser.rect.y < 0:
                lasers.remove(laser)
        lasers.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()