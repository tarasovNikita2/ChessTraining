from constants import *
import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, cell_size: int, color: str, field_name: str, file_postfix: str):
        super().__init__()
        picture = pygame.image.load(FIG_IMGS_PATH + color + file_postfix).convert_alpha()
        self.image = pygame.transform.smoothscale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.color = color
        self.field_name = field_name
        self.possible_moves = []


class King(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_king.png')
        self.name = 'K' if self.color == 'w' else 'k'


class Queen(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_queen.png')
        self.name = 'Q' if self.color == 'w' else 'q'


class Rock(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_rock.png')
        self.name = 'R' if self.color == 'w' else 'r'


class Bishop(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_bishop.png')
        self.name = 'B' if self.color == 'w' else 'b'


class Knight(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_knight.png')
        self.name = 'N' if self.color == 'w' else 'n'


class Pawn(Piece):
    def __init__(self, cell_size: int, color: str, field: str):
        super().__init__(cell_size, color, field, '_pawn.png')
        self.name = 'P' if self.color == 'w' else 'p'
