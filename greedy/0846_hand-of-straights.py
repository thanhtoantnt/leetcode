from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """Can hand be split into runs of groupSize consecutive values?

        Greedy on the smallest remaining card: every run containing it
        MUST start at it — count cards, then peel runs from the min
        upward, failing fast when a run breaks. O(n log n + n·k).
        """
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for start in sorted(count):
            need = count[start]
            if need <= 0:
                continue
            for v in range(start, start + groupSize):
                if count[v] < need:
                    return False
                count[v] -= need
        return True


if __name__ == "__main__":
    assert Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert not Solution().isNStraightHand([1, 2, 3, 4, 5], 4)
    print("ok")
