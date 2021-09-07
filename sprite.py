import pygame


# Class representing a sprite.
class Sprite:

    def __init__(self, surface, width, height, initial_x, initial_y):
        # Attributes
        self.surface = surface
        self.width = width
        self.height = height
        self.x_position = initial_x
        self.y_position = initial_y
        self.color = pygame.Color('white')
        self.rect = pygame.Rect((self.x_position, self.y_position), (self.width, self.height))

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x_pos(self):
        return self.x_position

    def get_y_pos(self):
        return self.y_position

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_x_pos(self, x):
        self.x_position = x

    def set_y_pos(self, y):
        self.y_position = y
