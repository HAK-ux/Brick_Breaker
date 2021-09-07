import pygame
import sprite
import window


# Class representing the paddle in the brick breaker game. (inherits Sprite class)
class Paddle(sprite.Sprite):

    def __init__(self, surface, width, height, initial_x, initial_y, screen):
        # Attributes
        super().__init__(surface, width, height, initial_x, initial_y)
        self.window = screen
        self.velocity = 0  # 0 initially
        self.accel = 7

    # Draw the paddle
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def move_left(self):
        self.velocity = -abs(self.accel)
        self.x_position += self.velocity
        self.rect.move_ip(self.velocity, 0)

    def move_right(self):
        self.velocity = abs(self.accel)
        self.x_position += self.velocity
        self.rect.move_ip(self.velocity, 0)

    def stop(self):
        self.velocity = 0

    def move(self):
        keys = pygame.key.get_pressed()

        # if A key is pressed
        if keys[pygame.K_a] and paddle.get_x_pos() >= 0:
            self.move_left()

        # if D key is pressed
        if keys[pygame.K_d] and paddle.get_x_pos() + paddle.get_width() <= window.width:
            self.move_right()


# Running the class
if __name__ == '__main__':
    pygame.init()
    # Create window
    window = window.Window()
    clock = pygame.time.Clock()
    # Create paddle
    paddle = Paddle(window.get_surface(), 40, 6, window.width / 2 - 20, window.height - 20, window)

    # Update display
    running = True
    while running:
        window.set_fps()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        paddle.move()
        window.get_surface().fill(pygame.Color('black'))
        paddle.draw()
        pygame.display.update()

    # quit pygame
    pygame.quit()
