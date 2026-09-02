import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    #GAME LOOP
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        pygame.display.flip()

        # limit the framerate to 60 FPS
        milliseconds = clock.tick(60)
        dt = milliseconds / 1000



if __name__ == "__main__":
    main()
