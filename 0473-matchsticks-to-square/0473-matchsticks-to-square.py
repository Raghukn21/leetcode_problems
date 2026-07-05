class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4
        # Sort descending: try longest sticks first — they're hardest to place,
        # so failing fast on them prunes the most branches early
        matchsticks.sort(reverse=True)

        # If any single stick is longer than a side, impossible
        if matchsticks[0] > side:
            return False

        sides = [0] * 4  # current running length of each of the 4 sides

        def backtrack(idx):
            if idx == len(matchsticks):
                # All sticks placed — check if all 4 sides are complete
                return sides[0] == sides[1] == sides[2] == sides[3] == side

            stick = matchsticks[idx]
            seen = set()  # skip sides that already have the same current length
                          # (trying the same length twice would produce identical subtrees)

            for i in range(4):
                if sides[i] + stick <= side and sides[i] not in seen:
                    seen.add(sides[i])
                    sides[i] += stick
                    if backtrack(idx + 1):
                        return True
                    sides[i] -= stick

            return False

        return backtrack(0)