class Solution:
    def checkValidString(self, s: str) -> bool:
        """Is s a valid parentheses string, where '*' may be '(', ')'
        or empty?

        Greedy range tracking: [lo, hi] = possible open-paren counts.
        '(' raises both; ')' lowers both; '*' widens: lo−1, hi+1.
        hi < 0 → too many forced closers → False; lo clamped at 0.
        Valid iff lo == 0 at the end. One pass, O(n)/O(1).
        """
        lo = hi = 0
        for ch in s:
            lo += 1 if ch == "(" else -1
            hi += 1 if ch != ")" else -1
            if hi < 0:
                return False  # even treating every '*' as '(' can't save it
            lo = max(lo, 0)
        return lo == 0  # some assignment lands exactly on zero


if __name__ == "__main__":
    assert Solution().checkValidString("()")
    assert Solution().checkValidString("(*)")
    assert Solution().checkValidString("(*))")
    assert not Solution().checkValidString("((*)")
    print("ok")
