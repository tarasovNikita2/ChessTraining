import pygame.display
import chess

from cell import *
from pieces import *

FONT18 = pygame.font.SysFont('verdana', 12)


def calculate_grade(prev_score, new_score):
    if prev_score <= new_score:
        return BEST_PATH
    elif prev_score <= new_score + 0.5:
        return EXCELLENT_PATH
    elif prev_score <= new_score + 1:
        return NORMAL_PATH
    elif prev_score <= new_score + 2:
        return INACCURACY_PATH
    elif prev_score <= new_score + 3:
        return MISTAKE_PATH
    elif prev_score > new_score + 3:
        return BLUNDER_PATH


class Chessboard:
    def __init__(self, parent_surface: pygame.Surface, board: chess.Board, engine, color,
                 cell_qty: int = CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_surface
        self.board = board
        self.__qty = cell_qty
        self.__size = cell_size
        self.__pieces_types = PIECES_TYPES
        self.__pressed_cell = None
        self.__picked_piece = None
        self.__all_cells = pygame.sprite.Group()
        self.all_pieces = pygame.sprite.Group()
        self.__all_areas = pygame.sprite.Group()
        self.color = 'w' if color == chess.WHITE else 'b'
        self.__draw_playboard()
        self.__draw_all_pieces()
        self.temp_grade = None
        self.last_cell = None
        self.engine = engine
        pygame.display.update()

    def __draw_playboard(self):
        total_width = self.__qty * self.__size
        self.__all_cells = self.__create_all_cells()

        playboard_view = pygame.Surface((total_width, total_width)).convert_alpha()

        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offset = (playboard_rect.x, playboard_rect.y)
        self.__draw_cells_on_playboard(cells_offset)

    def __create_all_cells(self):
        group = pygame.sprite.Group()
        cell_color_index = 1
        for y in range(self.__qty):
            for x in range(self.__qty):

                true_y = y if self.color == 'w' else 7 - y
                true_x = x if self.color == 'w' else 7 - x
                cell = Cell(cell_color_index, self.__size, (x, y), LTRS[true_x] + str(self.__qty - true_y))

                if x == self.__qty - 1:
                    row_number = FONT18.render(str(8 - true_y), True, CELL_COLORS[cell_color_index ^ True])
                    cell.image.blit(row_number, (self.__size - row_number.get_rect().width, 0))

                if y == self.__qty - 1:
                    row_number = FONT18.render(LTRS[true_x], True, CELL_COLORS[cell_color_index ^ True])
                    cell.image.blit(row_number, (0, self.__size - row_number.get_rect().height))

                group.add(cell)
                cell_color_index ^= True
            cell_color_index ^= True
        return group

    def __draw_cells_on_playboard(self, offset):
        for cell in self.__all_cells:
            cell.rect.x += offset[0]
            cell.rect.y += offset[1]
        self.__all_cells.draw(self.__screen)

    def __draw_all_pieces(self):
        self.__setup_board()
        self.all_pieces.draw(self.__screen)

    def __setup_board(self):
        self.all_pieces.empty()
        fen_board = self.board.board_fen()

        row = 0
        col = 0

        iterator = 1

        for i in fen_board:
            if str.isalpha(i):
                piece = self.__create_piece(i, (row, col))
                self.all_pieces.add(piece)
                col += iterator
            elif str.isdigit(i):
                col += int(i) * iterator
            else:
                col = 0
                row += iterator

        for piece in self.all_pieces:
            for cell in self.__all_cells:
                if piece.field_name == cell.field_name:
                    piece.rect = cell.rect

    def __create_piece(self, piece_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        piece_tuple = self.__pieces_types[piece_symbol]
        classname = globals()[piece_tuple[0]]
        return classname(self.__size, piece_tuple[1], field_name)

    def __to_field_name(self, table_coord: tuple):
        return LTRS[table_coord[1]] + str(self.__qty - table_coord[0])

    def __get_cell(self, position: tuple):
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell

        return None

    def btn_down(self, button_type: int, position: tuple):
        self.__pressed_cell = self.__get_cell(position)
        if self.__pressed_cell is None:
            return
        print('You click on' + self.__pressed_cell.field_name)

    def btn_up(self, button_type: int, position: tuple):
        released_cell = self.__get_cell(position)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 3:
                self.__mark_cell(released_cell)
            if button_type == 1:
                self.__pick_cell(released_cell)
        self.grand_update()

    def __mark_cell(self, cell):
        if not cell.mark:
            mark = Area(cell, 0)
            self.__all_areas.add(mark)
        else:
            for area in self.__all_areas:
                if area.field_name == cell.field_name:
                    area.kill()
                    break
        cell.mark ^= True

    def __unmark_all_cells(self):
        self.__all_areas.empty()
        for cell in self.__all_cells:
            cell.mark = False

    def grand_update(self):
        self.__all_cells.draw(self.__screen)
        self.__all_areas.draw(self.__screen)
        self.__draw_all_pieces()
        self.draw_grade(self.last_cell)
        pygame.display.update()

    def draw_grade(self, cell):
        if self.temp_grade == None:
            pass
        else:
            self.__screen.blit(self.temp_grade.image, cell.rect)

    def eval_position(self):
        info = self.engine.analyse(self.board, chess.engine.Limit(depth=24))
        return info["score"].white().score() / 100 if self.color == 'w' else info["score"].black().score() / 100


    def __pick_cell(self, cell):
        self.__unmark_all_cells()
        if self.__picked_piece is None:
            for piece in self.all_pieces:
                if piece.field_name == cell.field_name and piece.color == self.color:
                    pick = Area(cell, 1)
                    self.__all_areas.add(pick)

                    for move in self.board.legal_moves:
                        if move.uci().find(piece.field_name) != -1:
                            piece.possible_moves.append(move.uci().replace(piece.field_name, ''))

                    for temp_cell in self.__all_cells:
                        if temp_cell.field_name in piece.possible_moves:
                            sprite_index = 2
                            for temp_piece in self.all_pieces:
                                if temp_cell.rect == temp_piece.rect and piece.color != temp_piece.color:
                                    sprite_index = 3
                                    break

                            temp_pick = Area(temp_cell, sprite_index)
                            self.__all_areas.add(temp_pick)

                    self.__picked_piece = piece
                    break
        else:
            if cell.field_name in self.__picked_piece.possible_moves:
                for piece in self.all_pieces:
                    if piece.field_name == cell.field_name:
                        piece.kill()

                new_pos = cell.field_name
                old_pos = self.__picked_piece.field_name

                prev_score = self.eval_position()

                self.last_cell = cell
                self.__picked_piece.rect = cell.rect
                self.__picked_piece.field_name = cell.field_name
                move = chess.Move.from_uci(old_pos + new_pos)
                self.board.push(move)
                self.__picked_piece.possible_moves = []

                new_score = self.eval_position()

                path = calculate_grade(prev_score, new_score)

                self.temp_grade = Area(cell, 4, path)

            self.__picked_piece = None
