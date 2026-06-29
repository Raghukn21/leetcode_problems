class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        corners = set()
        total_area = 0
        
        min_x = min(r[0] for r in rectangles)
        min_y = min(r[1] for r in rectangles)
        max_x = max(r[2] for r in rectangles)
        max_y = max(r[3] for r in rectangles)
        
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            
            # Define the 4 corners of the current rectangle
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        
        # Check total area and the 4 corner points of the bounding box
        expected_area = (max_x - min_x) * (max_y - min_y)
        if total_area != expected_area:
            return False
            
        return (len(corners) == 4 and 
                (min_x, min_y) in corners and 
                (min_x, max_y) in corners and 
                (max_x, min_y) in corners and 
                (max_x, max_y) in corners)