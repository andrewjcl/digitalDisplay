import pygame


def draw_digit(screen, number):

    array = []

    match number:
        case 0:
            array = [False, False, False, False, False, False, False]
        case 1:
            array = [False, False, True, True, False, False, False]
        case 2:
            array = [True, False, True, False, True, True, True]

    # Draw all grey to start
    pygame.draw.line(screen, 'Grey', (100, 73), (100, 117), 5)
    pygame.draw.line(screen, 'Grey', (100, 15), (100, 60), 5)
    pygame.draw.line(screen, 'Grey', (140, 15), (140, 60), 5)
    pygame.draw.line(screen, 'Grey', (140, 73), (140, 117), 5)
    pygame.draw.line(screen, 'Grey', (98, 9), (142, 9), 5)
    pygame.draw.line(screen, 'Grey', (98, 66), (142, 66), 5)
    pygame.draw.line(screen, 'Grey', (98, 121), (142, 121), 5)

    # Then override with black depending on array values
    # 0 - BottomLeft
    if array[0]: pygame.draw.line(screen, 'black', (100, 73), (100, 117), 5)
    # 1 - TopLeft
    if array[1]: pygame.draw.line(screen, 'Black', (100, 15), (100, 60), 5)
    # 2 - TopRight
    if array[2]: pygame.draw.line(screen, 'Black', (140, 15), (140, 60), 5)
    # 3 - BottomRight
    if array[3]: pygame.draw.line(screen, 'Black', (140, 73), (140, 117), 5)
    # 4  Top
    if array[4]: pygame.draw.line(screen, 'Black', (98, 9), (142, 9), 5)
    # 5 - Middle
    if array[5]: pygame.draw.line(screen, 'Black', (98, 66), (142, 66), 5)
    # 6 - Bottom
    if array[6]: pygame.draw.line(screen, 'Black', (98, 121), (142, 121), 5)





