import pygame

#Warna default
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (173, 216, 230)
BLUE = (0, 100, 255)

class Node:
    def __init__(self, row, col, size ):
        self.row =row 
        self.col = col
        self.size = size 
        self.x = col * size 
        self.y = row * size
        self.status ="empty" 


    def draw(self, window):
        color = WHITE
        if self.status == "wall" :
            color = BLACK
        elif self.status == "start" :
            color = GREEN 
        elif self.status == "end" :
            color = RED
        elif self.status == "path" :
            color =YELLOW
        elif self.status == "frontier":
            color = LIGHT_BLUE
        elif self.status == "explored" :
            color = BLUE

        pygame.draw.rect(window, color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(window, (200,200,200), (self.x, self.y, self.size, self.size), 1)

    
    def toggle_wall(self):
        if self.status == "empty":
            self.status = "wall"
        elif self.status == "wall":
            self.status = "empty"

    def is_empty(self):
        return self.status == "empty"
    
    def is_wall(self):
        return self.status == "wall"
    
    def is_start(self):
        return self.status == "start"
    
    def is_end(self):
        return self.status == "end"
    

    def get_neighbors(self, grid, rows, cols):
        neighbors = [] 

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = self.row + dr, self.col + dc

            if (0 <= new_row < rows and 0 <= new_col < cols and not grid[new_row][new_col].is_wall()):
                neighbors.append(grid[new_row][new_col])  

        return neighbors 

    def set_explored(self):
        self.status = "explored"  

    def set_start(self):
        self.status = "start"

    def set_end(self):
        self.status = "end"

    def set_wall(self):
        self.status = "wall"

    def set_path(self):
        self.status = "path"

    def set_frontier(self):
        self.status = "frontier"

    def reset(self):
        self.status = "empty"

