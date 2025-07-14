import pygame
import sys  
from grid import make_grid, draw_grid
#inisialisasi pygame
pygame.init()

#konstanta ukuran window
WINDOW_SIZE = 600
WINDOW_TITLE = "Penentu Jalan Visualizer"
ROWS, COLS = 20, 20
CELL_SIZE = WINDOW_SIZE // ROWS 

# membuat Window 
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption(WINDOW_TITLE)

grid = make_grid(ROWS, COLS, CELL_SIZE)
grid[0][0].set_start()
grid[0][1].set_end()
grid[1][1].set_wall()
grid[2][2].set_path()

#Event Loop Dasar 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))
    draw_grid(window,grid)
    pygame.display.flip()

pygame.quit()
sys.exit()

