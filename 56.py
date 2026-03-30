def merge(self, intervals):
        if len(intervals)==1: return intervals
        intervals.sort()
        new = [intervals[0]]
        for start,end in intervals[1:]:
            if start <= new[-1][1]:
                new[-1][1] = max(new[-1][1],end)
            else:
                new.append([start,end])
        return new