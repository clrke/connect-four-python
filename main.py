import pygame

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

back = pygame.Surface((640,480))
background = back.convert()
background.fill((3,31,64))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]:
            pygame.quit()        
                    
    clock.tick(60)

