import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Digital Display')
clock = pygame.time.Clock()

bg_surf = pygame.Surface((400, 800))
bg_surf.fill('WHITE')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw background
    screen.blit(bg_surf, (0, 0))

    # TopLeft
    pygame.draw.line(screen, 'grey', (100, 15), (100, 60), 5)
    # TopRight
    pygame.draw.line(screen, 'Black', (140, 15), (140, 60), 5)
    # BottomLeft
    pygame.draw.line(screen, 'grey', (100, 73), (100, 117), 5)
    # BottomRight
    pygame.draw.line(screen, 'grey', (140, 73), (140, 117), 5)

    # Top
    pygame.draw.line(screen, 'Black', (98, 9), (142, 9), 5)
    # Middle
    pygame.draw.line(screen, 'Black', (98, 66), (142, 66), 5)

    # pygame.draw.circle(screen, 'Black', (200, 200), 6, 6)
    pygame.display.update()
    clock.tick(60)
