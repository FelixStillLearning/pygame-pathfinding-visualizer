from collections import deque
import time 
import pygame

from grid import draw_grid
from legend import draw_legend

class BFSAlgorithm :
    def __init__(self, grid, rows, cols):
        self.grid = grid 
        self.rows = rows 
        self.cols = cols 

        self.start_node = None 
        self.end_node = None
        self.path = None
        self.is_running = False
        self.is_complete = False

        self.queue = deque()
        self.visited = set() 
        self.parent= {}

    def find_start_end_nodes(self):
        self.start_node = None
        self.end_node = None

        for row in self.grid:
            for node in row:
                if node.is_start():
                    self.start_node = node 
                elif node.is_end():
                    self.end_node = node 

        return self.start_node is not None and self.end_node is not None
    
    def reset_algorithm_states(self):
        for row in self.grid:
            for node in row:
                if node.status in ["frontier", "explored", "path"]:
                    node.reset()

        self.path = None 
        self.is_complete = False 
        self.queue.clear()
        self.visited.clear()
        self.parent.clear()

    def initialize(self):

        if not self.find_start_end_nodes():
            print("ERROR missing start or end node!")
            return False 
        
        self.reset_algorithm_states()

        self.queue = deque([self.start_node])
        self.visited = {self.start_node}
        self.parent= {self.start_node: None}

        if self.start_node and self.end_node:
            print(f"✅ BFS initialized: Start({self.start_node.row}, {self.start_node.col}) → End({self.end_node.row}, {self.end_node.col})")
        return True
    

    def reconstruct_path(self):
        if not self.end_node or self.end_node not in self.parent:
            return None 
        
        path = []
        current = self.end_node

        while current is not None:
            path.append(current)
            current = self.parent.get(current)

        return path[::-1] 
    
    def visualize_path(self, path):
        if path:
            for node in path:
                if not node.is_start() and not node.is_end():
                    node.set_path()

    def execute_step(self):
        if not self.queue:
            print ("BFS selesai: tidak ada path")
            return "no_path"
        
        current_node = self.queue.popleft()
        
        # Type safety check (walau secara logika tidak mungkin None)
        if current_node is None:
            return "no_path"

        if current_node.is_end():
            self.path = self.reconstruct_path()
            self.visualize_path(self.path) 
            path_length = len(self.path) if self.path else 0
            print(f"🎯 BFS Berhasil: path ditemukan dengan {path_length} node")
            return "path_found"

        if not current_node.is_start():
            current_node.set_explored()

        neighbors = current_node.get_neighbors(self.grid, self.rows, self.cols)

        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.parent[neighbor] = current_node 
                self.queue.append(neighbor)

                if not neighbor.is_end():
                    neighbor.set_frontier()

        return "step_complete"
    
    def execute_with_visualization(self, window, font, delay=0.1):
        if not self.initialize():
            return None 
        
        self.is_running = True
        step_counter = 0

        print(" memulai visualisasi nya")

        while self.queue and self.is_running:
            step_counter += 1 
            result = self.execute_step()

            if result == "path_found":
                print(f"BFS selesai di langkah ke-{step_counter}")
                break

            elif result == "no_path":
                print(f"BFS selesai di langkah ke-{step_counter} - tidak ada path yang ditemukan")
                break

            elif result == "step_complete":
                # Continue the visualization
                pass 

            self._render_step(window, font, step_counter)
            time.sleep(delay)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running  = False
                    return None
                
        self.is_running = False 
        self.is_complete = True 
        return self.path 
    
    def _render_step(self, window, font , step_number ):
        window.fill((255,255,255))
        draw_grid(window,self.grid)
        draw_legend(window,font)

        step_text = font.render(f"BFS step: {step_number}", True, (0,0,0))
        window.blit(step_text,(10,10))

        queue_text = font.render(f"Queue Size: {len(self.queue)}", True, (0,0,0)) 
        window.blit(queue_text, (10,35))

        pygame.display.flip()

    def get_algorithm_info(self):
        return {
            "name": "Breadth-First Search (BFS)",
            "description": "Explores all neighbors at current depth before moving deeper",
            "pattern": "Level-by-level exploration (like ripples in water)",
            "data_structure": "Queue (FIFO - First In, First Out)",
            "time_complexity": "O(V + E) - visits each vertex and edge once",
            "space_complexity": "O(V) - queue and visited set storage",
            "guarantees_shortest_path": True,
            "best_for": "Unweighted graphs, shortest path finding",
            "visual_pattern": "Spreading outward from start in all directions equally"
        }

    def get_statistics(self):
        """
        Get algorithm execution statistics for educational analysis.
        
        Returns:
            dict: Statistics about the current/last algorithm run
        """
        return {
            "nodes_explored": len(self.visited),
            "path_length": len(self.path) if self.path else 0,
            "algorithm_complete": self.is_complete,
            "path_found": self.path is not None
        }
    


    

    


    

