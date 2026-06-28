from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, value: int) -> None:
        d = self.intervals

        # If value is already exactly the start of an existing interval,
        # it's definitely already covered — nothing to do.
        if value in d:
            return

        idx = d.bisect_left(value)
        keys = d.keys()

        # Check previous interval (the one whose start is just below 'value')
        merge_with_prev = False
        if idx > 0:
            prev_start = keys[idx - 1]
            prev_end = d[prev_start]
            if prev_end >= value:
                return  # already covered by the previous interval's range
            if prev_end == value - 1:
                merge_with_prev = True

        # Check next interval (the one whose start is just above 'value')
        merge_with_next = idx < len(keys) and keys[idx] == value + 1

        if merge_with_prev and merge_with_next:
            # Bridge the gap between prev and next — merge all three into one
            next_start = keys[idx]
            next_end = d[next_start]
            prev_start = keys[idx - 1]
            d[prev_start] = next_end
            del d[next_start]
        elif merge_with_prev:
            prev_start = keys[idx - 1]
            d[prev_start] = value
        elif merge_with_next:
            next_start = keys[idx]
            next_end = d[next_start]
            del d[next_start]
            d[value] = next_end
        else:
            d[value] = value

    def getIntervals(self) -> list[list[int]]:
        return [[start, end] for start, end in self.intervals.items()]