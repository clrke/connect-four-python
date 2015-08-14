import pygame
import pygame.draw

pygame.init()

GAME_WIDTH = 640
GAME_HEIGHT = 480
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), 0, 32)
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

GAME_MARGIN = 30
GAME_COLUMNS = 7
GAME_ROWS = 6

GAME_ROW_HEIGHT = (GAME_HEIGHT - GAME_MARGIN * 2) / (GAME_ROWS + 1)
GAME_COLUMN_WIDTH = (GAME_WIDTH - GAME_MARGIN * 2) / (GAME_COLUMNS + 1)

UPPER_BOUND = GAME_MARGIN
LEFT_BOUND = GAME_MARGIN
LOWER_BOUND = GAME_HEIGHT - GAME_MARGIN
RIGHT_BOUND = GAME_WIDTH - GAME_MARGIN

UPPER_LEFT_BOUND = (LEFT_BOUND, UPPER_BOUND)
UPPER_RIGHT_BOUND = (RIGHT_BOUND, UPPER_BOUND)
LOWER_LEFT_BOUND = (LEFT_BOUND, LOWER_BOUND)
LOWER_RIGHT_BOUND = (RIGHT_BOUND, LOWER_BOUND)

WHITE = (255, 255, 255)

back = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
background = back.convert()
background.fill((3, 31, 64))

pygame.draw.line(screen, WHITE, UPPER_LEFT_BOUND, LOWER_LEFT_BOUND, 5)
pygame.draw.line(screen, WHITE, LOWER_LEFT_BOUND, LOWER_RIGHT_BOUND, 5)
pygame.draw.line(screen, WHITE, LOWER_RIGHT_BOUND, UPPER_RIGHT_BOUND, 5)

pygame.draw.line(screen, WHITE, (LEFT_BOUND, UPPER_BOUND + GAME_ROW_HEIGHT * 1), (RIGHT_BOUND, UPPER_BOUND + GAME_ROW_HEIGHT * 1), 5)
for i in xrange(2, GAME_ROWS+7):
    pygame.draw.line(screen, WHITE, (LEFT_BOUND, UPPER_BOUND + GAME_ROW_HEIGHT * i), (RIGHT_BOUND, UPPER_BOUND + GAME_ROW_HEIGHT * i), 1)

for i in xrange(1, GAME_COLUMNS+1):
    pygame.draw.line(screen, WHITE, (LEFT_BOUND + GAME_COLUMN_WIDTH * i, UPPER_BOUND), (LEFT_BOUND + GAME_COLUMN_WIDTH * i, LOWER_BOUND), 1)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()

    clock.tick(60)
