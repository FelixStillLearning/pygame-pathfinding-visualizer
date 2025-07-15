import pygame
import sys  
from grid import make_grid, draw_grid, get_clicked_node, handle_mouse_click
from legend import draw_legend
from bfs_algorithm import BFSAlgorithm

#inisialisasi pygame
pygame.init()

#konstanta ukuran window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 650
WINDOW_TITLE = "Penentu Jalan Visualizer"
GRID_SIZE  = 600
ROWS, COLS = 20, 20
CELL_SIZE = GRID_SIZE // ROWS 

# membuat Window 
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Inisialisasi font untuk legend
font = pygame.font.Font(None, 24)

grid = make_grid(ROWS, COLS, CELL_SIZE)

# Initialize BFS Algorithm
bfs = BFSAlgorithm(grid, ROWS, COLS)

def reset_grid():
    """Reset grid to empty state"""
    for row in grid:
        for node in row:
            node.reset()
    bfs.reset_algorithm_states()
    print("🔄 Grid reset!")

#Event Loop Dasar 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            handle_mouse_click(mouse_pos, grid, CELL_SIZE, GRID_SIZE, event.button)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Run BFS Algorithm
                print("🚀 Starting BFS Algorithm...")
                path = bfs.execute_with_visualization(window, font, delay=0.1)
                if path:
                    print(f"✅ Path found with {len(path)} nodes!")
                else:
                    print("❌ No path found!")
            
            elif event.key == pygame.K_r:
                # Reset grid
                reset_grid()

    window.fill((255, 255, 255))
    draw_legend(window, font)
    draw_grid(window, grid)
    
    # Display controls
    controls_text = font.render("Controls: Left-Click=Wall, Right-Click=Start/End, SPACE=Run BFS, R=Reset", True, (0, 0, 0))
    window.blit(controls_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
sys.exit()

