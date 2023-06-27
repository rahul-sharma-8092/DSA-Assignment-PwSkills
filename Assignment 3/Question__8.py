# <<----function definition---->>
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


# <<----function calling---->>
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))
