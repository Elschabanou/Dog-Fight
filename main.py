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
        # create the two players
        self._player1 = Plane(self,300,30,0,0,0,1)
        self._player2 = Plane(self,300,30,0,0,0,2)


    def draw_player(self):
        pass

    def draw_background(self):
        # later use image of clouds
        self._screen.fill("lightblue")
        
    def run(self):
        
        while self._running:
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self._running = False

            # gets a list of all the buttons that are pressed
            self._keys = pygame.key.get_pressed()
            if self._keys[pygame.K_SPACE]: # Space to shoot for player 1
                self._player1.shoot()
            if self._keys[pygame.K_l]: # "l" to shoot for player 2
                self._player2.shoot()
            
            
            self.draw_background()
            pygame.display.flip()
            self._clock.tick(30) #Framerate
        
        pygame.quit()

        
if __name__ == "__main__":
    DogFight().run()