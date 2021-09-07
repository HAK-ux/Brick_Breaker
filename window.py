import pygame


# Class representing the window.
class Window:

    def __init__(self):
        # Attributes
        self.background = pygame.Color('black')
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.width = 500
        self.height = 400
        self.surface = pygame.display.set_mode((self.width, self.height))

        # Set window title
        pygame.display.set_caption('Brick Breaker')

    def get_surface(self):
        return self.surface

    def set_fps(self):
        self.game_Clock.tick(self.FPS)


# Running the class
if __name__ == '__main__':
    pygame.init()

    # Create window
    window = Window()

    # Update display
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()

    # quit pygame
    pygame.quit()
