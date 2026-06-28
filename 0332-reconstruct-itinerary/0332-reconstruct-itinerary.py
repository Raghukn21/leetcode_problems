import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        # Build adjacency list, using a min-heap for each airport's destinations
        # so we always have easy access to the lexicographically smallest unused option
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            # Greedily visit the smallest available destination first,
            # consuming it from the heap (since each ticket is used exactly once)
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            # Add this airport AFTER all its outgoing tickets have been used —
            # this postorder placement is what correctly handles dead-ends/backtracking
            route.append(airport)

        dfs("JFK")
        return route[::-1]  # reverse, since we built it in postorder (last-finished-first)