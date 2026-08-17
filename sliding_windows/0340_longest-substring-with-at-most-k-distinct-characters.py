class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Longest substring with at most k distinct characters
        (premium). 0003/0904's window generalized: count dict, shrink
        while len(count) > k. O(n).
        """
        if k == 0:
            return 0
        count: dict[str, int] = {}
        left = best = 0
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while len(count) > k:
                c = s[left]
                count[c] -= 1
                if not count[c]:
                    del count[c]
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstringKDistinct("eceba", 2) == 3  # "ece"
    assert Solution().lengthOfLongestSubstringKDistinct("aa", 1) == 2
    print("ok")
