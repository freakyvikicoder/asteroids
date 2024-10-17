import pygame
from constants import *
from player import *

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player.update(dt=dt)
        # player.draw(screen=screen)
        for updt in updatable:
            updt.update(dt=dt)
        
        screen.fill(color=(0,0,0))
        
        for drw in drawable:
            drw.draw(screen=screen)

        pygame.display.flip()
        deltaTime = gameClock.tick(60)
        dt = deltaTime / 1000
        

    

if __name__ == '__main__':
    main()