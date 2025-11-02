
def lengthOfLongestSubstring(self, s: str) -> int:  
    last_pos = {}
    start = 0
    result = 0

    for index, character in enumerate(s):
        if character in last_pos:
            # update start pos
            start = max(start, last_pos[character] + 1)

        last_pos[character] = index
        result = max(result, index + 1 - start)

    return result