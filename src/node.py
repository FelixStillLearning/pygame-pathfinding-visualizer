import pygame

#Warna default
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255, 255, 0)
PURPLE = (128,0 ,128)

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


    def set_start(self):
        self.status = "start"
    def set_end(self):
        self.status = "end"
    def set_wall(self):
        self.status = "wall"
    def set_path(self):
        self.status = "path"
    def reset(self):
        self.status = "empty"
