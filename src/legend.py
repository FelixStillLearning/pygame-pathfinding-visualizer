

import pygame

# Warna yang sama dengan node.py
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_legend(window, font):
    legend_data = [
        (WHITE, "Empty"),
        (GREEN, "Start"),
        (RED, "End"),
        (BLACK, "Wall"), 
        (YELLOW, "Path")
    ]

    start_x = 10 
    start_y = 620

    for i, (color, label) in enumerate(legend_data):
        rect_x = start_x + (i * 120)
        pygame.draw.rect(window, color, (rect_x, start_y, 20, 20))
        pygame.draw.rect(window, BLACK, (rect_x, start_y, 20, 20), 1)

        text_surface = font.render(label, True, BLACK)
        window.blit(text_surface, (rect_x + 25, start_y + 2))