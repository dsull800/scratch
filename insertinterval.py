class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_val = newInterval[0]
        left_search = True
        start_index = len(intervals) - 1
        index = start_index
        interval = newInterval
        for index, interval in enumerate(intervals):
            if left_search and newInterval[0] <= interval[1]:
                start_index = index
                print(start_index)
                start_val = min(newInterval[0], interval[0])
                left_search = False
            if not left_search and newInterval[1] >= interval[0]:
                if newInterval[1] >= interval[1]:
                    continue
                else:
                    if start_index == index:
                        # intervals.insert(start_index,[start_val, interval[1]])
                        intervals[start_index] = [start_val, interval[1]]
                        return intervals
                    intervals[start_index:index + 1] = [[start_val, interval[1]]]
                    return intervals
            elif not left_search and newInterval[1] < interval[0]:
                if start_index == index and start_val == newInterval[0]:
                    intervals[start_index] = [start_val, newInterval[1]]
                    return intervals
                else:
                    intervals.insert(start_index, [start_val, newInterval[1]])
                    return intervals
                intervals[start_index:index] = [[start_val, newInterval[1]]]
                return intervals

        if start_index == index and newInterval[0] > interval[1]:
            intervals.insert(start_index + 1, [start_val, newInterval[1]])
            return intervals
        elif start_index == index and newInterval[1] < interval[0]:
            intervals.insert(index - 1, [start_val, newInterval[1]])
            return intervals
        intervals[start_index:index + 1] = [[start_val, newInterval[1]]]
        return intervals

