from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Find the unique-if-it-exists starting station completing the
        circular route.

        Two facts: (1) a solution exists iff total gas ≥ total cost;
        (2) if a station A can't reach station B, no station between
        A and B can either — so on failure, resume from B+1.
        One pass, O(n).
        """
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


if __name__ == "__main__":
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    print("ok")
