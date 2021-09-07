import pygame
import sprite


# Class representing the paddle in the brick breaker game. (inherits Sprite class)
class Paddle(sprite.Sprite):

    def __init__(self, surface, width, height, initial_x, initial_y):
        # Attributes
        super().__init__(surface, width, height, initial_x, initial_y)
        self.surface = surface
        self.width = 6
        self.height = 40
        self.initialX = 0
        self.initialY = 0
        self.velocity = 0  # 0 initially
        self.accel = 7

    # Draw the paddle
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

# Running the class
if __name__ == '__main__':
    import window

    pygame.init()

    # create window
    w_surface = pygame.display.get_surface()
    window = window.Window(w_surface)
    window.create_window()

    pygame.display.update()
    paddle = Paddle(w_surface)
    paddle.draw()
    pygame.display.update()

    # quit pygame
    pygame.quit()
