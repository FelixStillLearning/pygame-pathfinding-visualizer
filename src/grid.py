import pygame
import sys 
from node import Node 

def make_grid(rows, cols, cell_size):
    return [[Node(row, col, cell_size) for col in range(cols)] for row in range (rows)]


def draw_grid(window, grid):
    for row in grid:
        for node in row:
            node.draw(window)