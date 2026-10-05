"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        #sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        #min heap to track end times
        min_heap = []
        #process each meeting 
        for meeting in intervals:
            # If a room is free (earliest ending meeting ends before current starts)
            if min_heap and min_heap[0] <= meeting.start:
                #reuse taht room/day
                heapq.heappop(min_heap)
            #allocate current meeting to a room/day
            heapq.heappush(min_heap, meeting.end)
        return len(min_heap)



        