class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        rooms = 0
        end_ptr = 0

        for s in start:
            if s < end[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1

        return rooms