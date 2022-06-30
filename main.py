import pygame
import digit
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Digital Display')
clock = pygame.time.Clock()

bg_surf = pygame.Surface((400, 800))
bg_surf.fill('WHITE')

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw background
    screen.blit(bg_surf, (0, 0))

    if count == 10: count = 0

    digit.draw_digit(screen, count)

    count += 1

    pygame.display.update()
    clock.tick(5)
