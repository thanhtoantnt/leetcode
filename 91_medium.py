class Solution:

    # 226 = (22| 6) + (2|26) = (22|6) + (2|(2|6 + 26))
    # 
    def numDecodings(self, s: str) -> int:
        # Your code here
        dp = [0] * (len(s) + 1)

        for length in range(1, len(s) + 1):
            s_index = len(s) - length
            # print(f"len = {length} with index = {s_index} with s[s_index] == {s[s_index]}")
            if s[s_index] == '0':
                dp[length] = 0
                # print(f"return 0")
                continue

            if length == 1:
                dp[length] = 1
                continue

            fst_case = dp[length - 1]
            snd_case = 0

            if s_index + 2 < len(s)+1 and length - 2 >= 0:
                num = int(s[s_index:(s_index+2)])
                if (num >= 1 and num <= 26):
                    if length-2 == 0:
                        snd_case = 1
                    else:
                        snd_case = dp[length-2]

            # print(f"fst_case = {fst_case} and snd_case = {snd_case}")
            dp[length] = fst_case + snd_case

        return dp[len(s)]

class SolutionOpt:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has 1 way to decode
        
        for i in range(1, n + 1):
            # Single digit decoding
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two digit decoding
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))    # Expected: 2
    print(sol.numDecodings("226"))   # Expected: 3
    print(sol.numDecodings("06"))    # Expected: 0
    print(sol.numDecodings("0"))     # Expected: 0
    print(sol.numDecodings("10"))    # Expected: 1
    print(sol.numDecodings("27"))    # Expected: 1
                
