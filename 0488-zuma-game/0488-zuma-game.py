from collections import deque

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s: str) -> str:
            changed = True
            while changed:
                changed = False
                i = 0
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        s = s[:i] + s[j:]
                        changed = True
                        break
                    i = j
            return s

        start_hand = "".join(sorted(hand))
        queue = deque([(board, start_hand, 0)])
        visited = {(board, start_hand)}

        while queue:
            b, h, steps = queue.popleft()
            
            if not b:
                return steps

            for i in range(len(b) + 1):
                for j in range(len(h)):
                    # Skip duplicate balls in hand
                    if j > 0 and h[j] == h[j - 1]:
                        continue
                    
                    # Correct pruning condition:
                    # Only insert h[j] if it matches b[i] or b[i-1], 
                    # OR if it's adjacent to the same color ball.
                    # Do not use restrictive checks that block valid bridge placements.
                    can_insert = False
                    if i > 0 and b[i - 1] == h[j]:
                        can_insert = True
                    elif i < len(b) and b[i] == h[j]:
                        can_insert = True
                    # Optimization condition that safely allows necessary placements
                    elif i > 0 and i < len(b) and b[i - 1] == b[i] and b[i] != h[j]:
                        # Allows inserting between different colored blocks if needed
                        can_insert = True
                    
                    # If none of the relaxed neighborhood conditions match, it's safe to skip
                    if not can_insert and (i > 0 and i < len(b) and b[i-1] != h[j] and b[i] != h[j]):
                        continue

                    new_board = clean(b[:i] + h[j] + b[i:])
                    new_hand = h[:j] + h[j + 1:]
                    
                    if (new_board, new_hand) not in visited:
                        visited.add((new_board, new_hand))
                        queue.append((new_board, new_hand, steps + 1))

        return -1