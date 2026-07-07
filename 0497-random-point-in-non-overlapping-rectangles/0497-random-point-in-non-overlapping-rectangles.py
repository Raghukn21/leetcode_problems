import random
import bisect

class Solution:
    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.weights = []
        total_points = 0
        
        for a, b, x, y in rects:
           
            points = (x - a + 1) * (y - b + 1)
            total_points += points
            self.weights.append(total_points)
            
        self.total_points = total_points

    def pick(self) -> list[int]:
        
        choice = random.randint(1, self.total_points)
        
       
        rect_index = bisect.bisect_left(self.weights, choice)
        a, b, x, y = self.rects[rect_index]
        
        
        prev_weight = self.weights[rect_index - 1] if rect_index > 0 else 0
        offset = choice - prev_weight - 1
        
        
        width = x - a + 1
        u = a + (offset % width)
        v = b + (offset // width)
        
        return [u, v]