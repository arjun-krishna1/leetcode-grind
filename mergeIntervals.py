'''
GIVEN
INPUT
intervals: intervals[i] = [start of i'th interval, end of i'th interval]
merge all overlapping intervals

OUTPUT
return an array of the non-overlapping intervals that cover all the intervals in the input

EXAMPLE
1:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
already sorted
the end of intervals[0] is after the start of intervals[1] and before the end of intervals[1], these two can be merged
    the lowest start time is 1, the highest end time is 6
    so [1, 3] and [2, 6] can be merged to [1, 6]
intervals = [[1, 6], [8, 10], [15, 18]]
all of the end times of the rest intervals are before the start times of the next interval
6 < 8, 10 < 15
it is done
return [[1, 6], [8, 10], [15, 18]]

2:
already sorted
[[1, 4], [4, 5]] -> [1, 5]
intervals[0][1] >= intervals[1][0]: they are overlapping
erge them -> [[1, 5]]

BRUTE FORCE
    while we haven't considered all of the intervals left
        find each other interval whose start time is before this ones end time
        and its end time is after this end time
        i.e. they are overlapping
        
        find the smallest start time out of all of these overlapping interval
        find the largest end time out of all of these overlapping intervals
        replace all of these overlapping interval with the smallest start time and the largest end time
        move to the next interval
    return intervals
    
SORTING O(n**2) time (single iteration, popping non-end element from list) O(1) space
    sort intervals
    while we have intervals left to consider
        if the next intervals start time is before this ones end time
            merge these two
        else
            move to the next one
    return intervals
    
OPTIMIZATION
    push result into another list -> O(n) time, O(n) space
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort intervals
        intervals.sort()
        
        result = []
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        
        # iterate through each interval
        for i in range(len(intervals)):
            # this interval is overlapping with the previous interval
            if end_time >= intervals[i][0]:
                end_time = max(end_time, intervals[i][1])
            # not merged
            else:
                # add the previous merged interval to result
                result.append([start_time, end_time])
                # update start and end time of this interval
                start_time = intervals[i][0]
                end_time = intervals[i][1]
        # add the last interval
        result.append([start_time, end_time])
        return result
