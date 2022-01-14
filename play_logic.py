import chess
import pygame
import chess.engine
from chessboard import Chessboard
from constants import *


def play(screen, clock, color):
    engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)
    board = chess.Board()
    chessboard = Chessboard(screen, board, engine, color)

    while not board.is_game_over():
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if board.turn == color:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    chessboard.btn_down(event.button, event.pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    chessboard.btn_up(event.button, event.pos)
            else:
                result = engine.play(board, chess.engine.Limit(time=0.1))
                board.push(result.move)
                chessboard.grand_update()
