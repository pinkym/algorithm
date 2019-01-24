# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: Sorted interval list.
    @param new_interval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            intervals.insert(0, new_interval)
            return intervals

        start_index = 0
        while start_index < len(intervals) and intervals[start_index].start < new_interval.start and \
                intervals[start_index].end < new_interval.start:
            start_index += 1

        end_index = start_index
        while end_index < len(intervals) and intervals[end_index].start < new_interval.end \
                and intervals[end_index].end < new_interval.end:
            end_index += 1

        # confirm new start
        if start_index == len(intervals):
            new_start = new_interval.start
        elif new_interval.start < intervals[start_index].start:
            new_start = new_interval.start
        else:
            new_start = intervals[start_index].start
        # confirm new end
        if end_index == len(intervals):
            new_end = new_interval.end
        elif new_interval.end < intervals[end_index].start:
            new_end = new_interval.end
        else:
            new_end = intervals[end_index].end

        # merge
        if not start_index == end_index:
            del_end_index = end_index
            if end_index < len(intervals) and not new_interval.end < intervals[end_index].start:
                del_end_index = end_index + 1
            for i in range(start_index, del_end_index):
                del intervals[start_index]
        elif start_index == end_index and len(intervals) == end_index:
            pass
        elif start_index == end_index and intervals[end_index].start <= new_interval.end <= intervals[end_index].end:
            del intervals[start_index]

        intervals.insert(start_index, Interval(new_start, new_end))
        return intervals


if __name__ == "__main__":

    intervals = [Interval(1, 3), Interval(5, 7), Interval(10, 13)]
    new_i = Interval(2, 9)
    s = Solution()

    print(s.insert(intervals, new_i))
