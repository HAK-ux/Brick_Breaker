import pygame


# Class representing the window.
class Window:

    def __init__(self, surface):
        # Attributes
        self.surface = surface
        self.background = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.exit = False
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


# Running the class
if __name__ == '__main__':
    pygame.init()

    # create window
    w_surface = pygame.display.get_surface()
    window = Window(w_surface)
    window.create_window()

    # quit pygame
    pygame.quit()
