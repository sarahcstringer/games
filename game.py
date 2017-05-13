import pygame
import random

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
        self.image = pygame.Surface([2, 20])
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
        self.velocity = 1

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

    # def bounce(self):
    #     """Bounce"""

    #     y = self._bounce()
    #     self.rect.y = next(y)

    def _bounce(self):
        gravity = .1
        slow = 0.9

        self.rect.y = self.rect.y + self.velocity
        if self.rect.y > size[1] - self.size:
            self.velocity = -self.velocity*slow
        else:
            self.velocity = self.velocity + gravity


def main():

    # start the game
    pygame.init()

    # screen settings

    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    pygame.display.set_caption('Pew Pew')

    clock = pygame.time.Clock()

    done = False

    lasers = pygame.sprite.Group()
    spaceships = pygame.sprite.Group()
    player = Spaceship()
    spaceships.add(player)

    # create blobs
    blobs = pygame.sprite.Group()
    blob_start_x = range(size[0])
    blob_start_y = range(size[1]/3)

    # ending game
    wait = 0
    killed = False
    for i in range(3):
        blob = Blob(random.choice(blob_start_x), random.choice(blob_start_y))
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

        def process_blobs():
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
                blob.move()
                blob._bounce()
            blobs.draw(screen)

        screen.fill(BLACK)
        spaceships.draw(screen)
        player_kill = pygame.sprite.spritecollide(player, blobs, True)
        if player_kill:
            killed = True
            
        if killed:
            player.image.fill(RED)
            if wait < 100:
                blobs.draw(screen)
                wait += 1
            else:
                blobs = pygame.sprite.Group()
        else:
            process_blobs()

        

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