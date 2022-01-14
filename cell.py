import pygame
from constants import *

pygame.init()


class Cell(pygame.sprite.Sprite):
    def __init__(self, color_index: int, size: int,
                 coords: tuple, name: str):
        super().__init__()
        x, y = coords
        self.color = color_index
        self.field_name = name
        self.image = pygame.image.load(CELL_IMGS[color_index])
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = pygame.Rect(x * size, y * size, size, size)
        self.mark = False


class Area(pygame.sprite.Sprite):
    def __init__(self, cell: Cell, type_of_area: int, grade_type: str = ''):
        super().__init__()
        coords = (cell.rect.x, cell.rect.y)
        area_size = (cell.rect.width, cell.rect.height)
        if type_of_area == 0:
            picture = pygame.image.load(CIRCLE_IMG_PATH).convert_alpha()
            self.image = pygame.transform.smoothscale(picture, area_size)
        elif type_of_area == 1:
            self.image = pygame.Surface(area_size).convert_alpha()
            self.image.fill(ACTIVE_CELL_COLOR)
        elif type_of_area == 2:
            surface = pygame.Surface(area_size, pygame.SRCALPHA)
            pygame.draw.circle(surface, ACTIVE_CELL_COLOR, (area_size[0] / 2, area_size[1] / 2), area_size[0] / 8)
            self.image = surface
        elif type_of_area == 3:
            surface = pygame.Surface(area_size, pygame.SRCALPHA)
            pygame.draw.rect(surface, ACTIVE_CELL_COLOR, (0, 0, area_size[0], area_size[1]), 6)
            self.image = surface
        elif type_of_area == 4:
            picture = pygame.image.load(grade_type).convert_alpha()
            self.image = pygame.transform.smoothscale(picture, (area_size[0] // 3, area_size[0] // 3))

        self.rect = pygame.Rect(coords, area_size)
        self.field_name = cell.field_name
