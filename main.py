import pygame
from Commands import Command

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Learn and code")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

square_size = 50
square_x = 50
square_y = 250

command = Command()

font = pygame.font.SysFont(None, 32)

input_rect = pygame.Rect(400, 100, 300, 50)
input_text = ''
input_active = False

clock = pygame.time.Clock()

run = True
while run:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if win.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((800, 600))
                else:
                    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            if event.key == pygame.K_RETURN:
                square_x, square_y = command.movecommand(input_text, square_x, square_y)
                command.intcommand(input_text)
                command.forcommand(input_text)

                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False

    win.fill(WHITE)

    pygame.draw.rect(win, RED, (square_x, square_y, square_size, square_size))

    pygame.draw.rect(win, BLACK, input_rect, 2)
    text_surface = font.render(input_text, True, BLACK)
    win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.draw.line(win, BLACK, (input_rect.x, input_rect.y + input_rect.height), (input_rect.x + input_rect.width, input_rect.y + input_rect.height), 2)

    pygame.display.update()

pygame.quit()
