import unittest
import chess


class MyTestCase(unittest.TestCase):
    def test_pawn_moves(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/1ppppppp/p7/8/8/P7/1PPPPPPP/RNBQKBNR w KQkq - 0 2')

        legal_move = chess.Move.from_uci('a3a4')
        fake_move = chess.Move.from_uci('a3a5')
        check_legal = legal_move in board.legal_moves
        check_fake = fake_move not in board.legal_moves

        self.assertEqual(True, check_legal)
        self.assertEqual(True, check_fake)

    def test_pawn_first_move(self):
        board = chess.Board()
        legal_move = chess.Move.from_uci('a2a4')
        check_legal = legal_move in board.legal_moves
        self.assertEqual(True, check_legal)

    def test_pawn_take(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2')
        legal_move = chess.Move.from_uci('e4d5')
        check_legal = legal_move in board.legal_moves
        self.assertEqual(True, check_legal)

    def test_pawn_extra_take(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/1pp1pppp/8/p2pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3')
        legal_move = chess.Move.from_uci('e5d6')
        check_legal = legal_move in board.legal_moves
        self.assertEqual(True, check_legal)

    def test_knight_moves(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/1pppppp1/p6p/4N3/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 3')

        legal_moves = ['e5g4', 'e5g6', 'e5f7', 'e5d7', 'e5c6', 'e5c4', 'e5d3', 'e5f3']
        check_legal = True

        for move in legal_moves:
            if chess.Move.from_uci(move) not in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_bishop_moves(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/2ppppp1/pp5p/4B3/8/3P4/PPP1PPPP/RN1QKBNR w KQkq - 0 4')

        legal_moves = ['e5d6', 'e5d4', 'e5c3', 'e5f4', 'e5c7', 'e5g7', 'e5g3', 'e5f6']
        check_legal = True

        for move in legal_moves:
            if chess.Move.from_uci(move) not in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_rock_moves(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/2pppp2/pp4pp/4R3/7P/8/PPPPPPP1/RNBQKBN1 w Qkq - 0 5')

        legal_moves = ['e5e6', 'e5e7', 'e5e3', 'e5e4', 'e5a5', 'e5b5', 'e5c5', 'e5d5', 'e5f5', 'e5g5', 'e5h5']
        check_legal = True

        for move in legal_moves:
            if chess.Move.from_uci(move) not in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_queen_moves(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/2ppppp1/pp5p/4Q3/8/4P3/PPPP1PPP/RNB1KBNR w KQkq - 0 4')

        legal_moves = ['e5e6', 'e5e7', 'e5e4', 'e5a5', 'e5b5', 'e5c5', 'e5d5', 'e5f5', 'e5g5', 'e5h5',
                       'e5d6', 'e5d4', 'e5c3', 'e5f4', 'e5c7', 'e5g7', 'e5g3', 'e5f6']
        check_legal = True

        for move in legal_moves:
            if chess.Move.from_uci(move) not in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_king_moves(self):
        board = chess.Board()
        board.set_fen('rn1qkbnr/1bpppp2/pp4pp/4K3/8/4P3/PPPP1PPP/RNBQ1BNR w kq - 2 6')

        legal_moves = ['e5d4', 'e5f4']
        check_legal = True

        for move in legal_moves:
            if chess.Move.from_uci(move) not in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_king_check_moves(self):
        board = chess.Board()
        board.set_fen('rn1qkbnr/1bpppp2/pp4pp/4K3/8/4P3/PPPP1PPP/RNBQ1BNR w kq - 2 6')

        check_moves = ['e5d5', 'e5d6', 'e5e6', 'e5f6', 'e5f5', 'e5e4']
        check_legal = True

        for move in check_moves:
            if chess.Move.from_uci(move) in board.legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)

    def test_castling(self):
        board = chess.Board()
        board.set_fen('rnbqkbnr/1ppp1pp1/p6p/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4')

        castling_move = 'e1g1'

        check_legal = chess.Move.from_uci(castling_move) in board.legal_moves

        self.assertEqual(True, check_legal)

    def test_check_castling(self):
        board = chess.Board()
        board.set_fen('rnbqk1nr/2pp1pp1/pp5p/2b1N3/2B1P3/5P2/PPPP2PP/RNBQK2R w KQkq - 1 6')

        castling_move = 'e1g1'

        check_legal = chess.Move.from_uci(castling_move) in board.legal_moves

        self.assertEqual(False, check_legal)

    def test_impossible_castling(self):

        board = chess.Board()
        board.set_fen('rnbqk1nr/2pp1pp1/8/p1p1N2p/2B1P3/5P2/P1PP2PP/RNBQK2R b kq - 1 9')

        castling_move = 'e1g1'

        check_legal = chess.Move.from_uci(castling_move) in board.legal_moves

        self.assertEqual(False, check_legal)

    def test_check_escaping(self):
        board = chess.Board()
        board.set_fen('rnbqk1nr/2pp1B2/6p1/p1p1N2p/4P3/5P2/P1PP2PP/RNBQK2R b kq - 0 10')

        legal_moves = ['e8e7', 'e8f8']
        check_legal = True

        for move in board.legal_moves:
            if move.uci() not in legal_moves:
                check_legal = False

        self.assertEqual(True, check_legal)


if __name__ == '__main__':
    unittest.main()
