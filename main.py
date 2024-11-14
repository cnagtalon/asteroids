# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)


    # Create the player before the game loop
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    #the game loop
    while True:
        dt = (clock.tick(60) /1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for sprite in updatable:
            sprite.update(dt)
            
        screen.fill(BLACK)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()











if __name__ == "__main__":
    main()