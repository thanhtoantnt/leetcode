from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """Split s into max parts so each letter appears in one part only.

        First compute each letter's last occurrence; sweep keeping the
        running furthest-last: a part may close exactly when the index
        reaches that frontier (no letter inside extends further).
        O(n).
        """
        last = {ch: i for i, ch in enumerate(s)}
        out = []
        start = 0
        reach = 0
        for i, ch in enumerate(s):
            reach = max(reach, last[ch])
            if i == reach:
                out.append(i - start + 1)
                start = i + 1
        return out


if __name__ == "__main__":
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    print("ok")
