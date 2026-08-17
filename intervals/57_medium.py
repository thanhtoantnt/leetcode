from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        nStart = newInterval[0]
        nEnd = newInterval[1]

        stop = False

        for interval in intervals:
            if stop:
                result.append(interval)
                continue

            start = interval[0]
            end = interval[1]

            if end < nStart:
                result.append(interval)
            
            elif start > nEnd:
                result.append([nStart, nEnd])
                result.append(interval)
                stop = True
            else:
                nStart = min(start, nStart)
                nEnd = max(end, nEnd)

        if not stop:
            result.append([nStart, nEnd])
        
        return result
            

        