import pygame
import sys 
from node import Node 

def make_grid(rows, cols, cell_size):
    return [[Node(row, col, cell_size) for col in range(cols)] for row in range (rows)]


def draw_grid(window, grid):
    for row in grid:
        for node in row:
            node.draw(window)

def get_clicked_node(mouse_pos, grid, cell_size, grid_size):
    x,y = mouse_pos
    if y < grid_size :
        row = y // cell_size 
        col = x // cell_size
        return grid[row][col] if 0 <= row < len(grid) and 0 <= col < len(grid[0]) else None
    return None

def handle_mouse_click(mouse_pos, grid, cell_size, grid_size, button):
    clicked_node = get_clicked_node(mouse_pos, grid, cell_size, grid_size)
    if clicked_node:
        if button == 1:
            if clicked_node.status not in ["start", "end"]:
                clicked_node.toggle_wall()
        elif button == 3:
            if clicked_node.status == "empty":
                clicked_node.set_start()
            elif clicked_node.status == "start":
                clicked_node.set_end ()
            elif clicked_node.status == "end":
                clicked_node.set_end()
                