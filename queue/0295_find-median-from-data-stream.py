import heapq


class MedianFinder:
    """Running median of a stream. Two heaps:

    lo  — max-heap of the smaller half (negated in Python)
    hi  — min-heap of the larger half
    Invariant: len(lo) == len(hi) or len(lo) == len(hi)+1; every element
    of lo <= every element of hi. Median = lo top (odd) or the two tops'
    average. addNum O(log n), findMedian O(1).
    """

    def __init__(self):
        self.lo: list[int] = []
        self.hi: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))  # move max of lo to hi
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))  # rebalance sizes

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2


if __name__ == "__main__":
    m = MedianFinder()
    for x in (1, 2, 3):
        m.addNum(x)
    assert m.findMedian() == 2.0
    m.addNum(4)
    assert m.findMedian() == 2.5
    print("ok")
