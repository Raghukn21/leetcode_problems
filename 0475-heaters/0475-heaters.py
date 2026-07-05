import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find the position where the house would fit in the sorted heaters
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right (if exists)
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            # Distance to the heater on the left (if exists)
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # The house is covered by the closest heater
            min_dist = min(dist_left, dist_right)
            
            # The required radius must be at least the max of these min distances
            max_radius = max(max_radius, min_dist)
            
        return max_radius