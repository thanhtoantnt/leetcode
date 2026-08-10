from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_table = {}
        start = 0
        max_sum = 0
    
        for index, num in enumerate(fruits):
            hash_table[num] = hash_table.get(num, 0) + 1

            while len(hash_table) > 2:
                # remove the element at fruits[start]
                start_elem = fruits[start]
                hash_table[start_elem] = hash_table.get(start_elem) - 1
                if hash_table[start_elem] == 0:
                    hash_table.pop(fruits[start])
                
                start += 1
            
            max_sum = max(max_sum, index + 1 - start)

        return max_sum
            

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1,2,1]))          # Expected: 3
    print(sol.totalFruit([0,1,2,2]))        # Expected: 3  
    print(sol.totalFruit([1,2,3,2,2]))      # Expected: 4
    print(sol.totalFruit([3,1,2,1,1,2,3,3])) # Expected: 5