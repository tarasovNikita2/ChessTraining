import random
from play_logic import *

color_rand = random.randint(0, 1)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_SIZE)

screen.fill(BACKGROUND_COLOR)

color = chess.WHITE if color_rand == 1 else chess.BLACK
play(screen, clock, color)
