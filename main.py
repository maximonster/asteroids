# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    pewpew = pygame.sprite.Group()
    Player.containers =(updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers =(pewpew, updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for up in updatable:
            up.update(dt)
        for ast in asteroids:
            for pew in pewpew:
                if(ast.collission(pew)):
                    ast.split()
                    pew.kill()
            if(ast.collission(player)):
                print("Game over!")
                return
        screen.fill(color=pygame.Color(0,0,0))
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()