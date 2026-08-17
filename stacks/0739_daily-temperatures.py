class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        result = [0] * len(temperatures)

        for index, value in enumerate(temperatures):
            # [38, 30] 36
            while stack and stack[-1][1] < value:
                day, _ = stack.pop()
                result[day] = index - day
            stack.append((index, value))

        return result