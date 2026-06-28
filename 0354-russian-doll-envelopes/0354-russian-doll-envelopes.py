from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Sort by width ascending; for ties in width, sort by height DESCENDING
        envelopes.sort(key=lambda e: (e[0], -e[1]))

        heights = [e[1] for e in envelopes]

        # Now find the Longest Increasing Subsequence of heights
        tails = []  # tails[i] = smallest possible tail value of an increasing subsequence of length i+1
        for h in heights:
            pos = bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h

        return len(tails)