import pygame


# Class which initializes the window
class Window:

    def __init__(self):
        # Class Attributes
        self.background = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.running = True
        self.width = 500
        self.height = 400

    def create_window(self):
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Brick Breaker')

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


# Testing the class
if __name__ == '__main__':
    pygame.init()
    # create window
    window = Window()
    window.create_window()
    # quit pygame and clean up the pygame window
    pygame.quit()
