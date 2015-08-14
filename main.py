import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

back = pygame.Surface((640, 480))
background = back.convert()
background.fill((3, 31, 64))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
        pygame.quit()

    clock.tick(60)
