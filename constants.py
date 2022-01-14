WINDOW_SIZE = (700, 700)
BACKGROUND_COLOR = (230, 230, 250)

FPS = 30

CELL_QTY = 8
CELL_SIZE = 70
WHITE_CELL_COLOR = (161, 167, 185)
BLACK_CELL_COLOR = (44, 44, 50)
ACTIVE_CELL_COLOR = (224, 16, 64)
CELL_COLORS = [BLACK_CELL_COLOR, WHITE_CELL_COLOR]

BLACK_CELL_IMG_PATH = 'Cells/BlackCell.png'
WHITE_CELL_IMG_PATH = 'Cells/WhiteCell.png'
CELL_IMGS = [BLACK_CELL_IMG_PATH, WHITE_CELL_IMG_PATH]


LTRS = 'abcdefgh'

PIECES_TYPES = {
    'k':('King', 'b'), 'K':('King', 'w'),
    'q':('Queen', 'b'), 'Q':('Queen', 'w'),
    'r':('Rock', 'b'), 'R':('Rock', 'w'),
    'b':('Bishop', 'b'), 'B':('Bishop', 'w'),
    'n':('Knight', 'b'), 'N':('Knight', 'w'),
    'p':('Pawn', 'b'), 'P':('Pawn', 'w')}

LETTERS_TO_NUMBERS = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7}

NUMBERS_TO_LETTERS = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'}

FIG_IMGS_PATH = 'ChessFig/'

CIRCLE_IMG_PATH = 'Marks/red_circle.png'

ENGINE_PATH = r"C:\Users\tnetm\Downloads\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe"

BEST_PATH = 'Grades/best.png'
BLUNDER_PATH = 'Grades/blunder.png'
EXCELLENT_PATH = 'Grades/excellent.png'
INACCURACY_PATH = 'Grades/inaccuracy.png'
MISTAKE_PATH = 'Grades/mistake.png'
NORMAL_PATH = 'Grades/normal.png'

