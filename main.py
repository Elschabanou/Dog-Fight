import pygame
# to insatll pygame: "pip install pygame"
from plane import Plane
print("Hallo Dog-Fight")


# a useful comment

class DogFight():
    
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((500, 500))
        self._clock = pygame.time.Clock()
        self._running = True

    def draw(self):
        self._screen.fill("purple")
        
    def run(self):
        
        while self._running:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self._running = False
            
            self._screen.fill("lightblue")
            pygame.display.flip()
            self._clock.tick(60)
        
        pygame.quit()

        
if __name__ == "__main__":
    DogFight().run()