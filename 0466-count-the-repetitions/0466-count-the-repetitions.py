class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len1, len2 = len(s1), len(s2)

        seen = {}
        s2_idx = 0
        s2_count = 0

        for s1_count in range(n1):
            if s2_idx in seen:
                prev_s1_count, prev_s2_count = seen[s2_idx]

                cycle_len = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count

                remaining_s1 = n1 - s1_count
                full_cycles = remaining_s1 // cycle_len
                leftover_s1 = remaining_s1 % cycle_len

                s2_count += full_cycles * cycle_s2

                for _ in range(leftover_s1):
                    for ch in s1:
                        if ch == s2[s2_idx]:
                            s2_idx += 1
                            if s2_idx == len2:
                                s2_count += 1
                                s2_idx = 0

                return s2_count // n2

            seen[s2_idx] = (s1_count, s2_count)

            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len2:
                        s2_count += 1
                        s2_idx = 0

        return s2_count // n2