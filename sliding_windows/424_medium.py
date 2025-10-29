class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        start = 0
        longest = 0
        
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])
            
            while (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                # Update max_freq - would need to find new max in freq.values()
                max_freq = max(freq.values())  # This is O(26) operation
                start += 1
            
            longest = max(longest, end - start + 1)
        
        return longest