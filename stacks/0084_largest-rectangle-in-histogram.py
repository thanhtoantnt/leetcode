from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Largest rectangle under a histogram. O(n) monotonic stack.

        Keep a stack of bars with increasing heights. When a shorter bar
        arrives, the taller stacked bars can't extend right past it:
        pop each and compute width = distance to the new bar's left
        boundary (the new stack top) — heights[pop] * width.
        """
        stack = []  # indices, heights increasing
        best = 0
        for i, h in enumerate(heights + [0]):  # sentinel flush at the end
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (i - left - 1))
            stack.append(i)
        return best


if __name__ == "__main__":
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea([2, 4]) == 4
    print("ok")
