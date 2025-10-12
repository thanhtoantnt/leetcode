from typing import List
from collections import defaultdict

class Solution:
    def shift_letter(self, letter, shift):
        # Determine base
        base = ord('a')
        
        # Calculate position in alphabet (0-25), apply shift, and wrap around
        position_in_alphabet = ord(letter) - base
        new_position = (position_in_alphabet + shift) % 26
        
        # Convert back to character
        new_letter = chr(base + new_position)
        return new_letter
    
    def shift_word(self, word, shift):
        return ''.join(self.shift_letter(letter, shift) for letter in word)

    # def shift_word(self, word, shift):
    #     result = []
    #     for letter in word:
    #         shifted_letter = self.shift_letter(letter, shift)
    #         result.append(shifted_letter)
    #     return ''.join(result)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strings:
            shift = ord('a') - ord(word[0])
            key = self.shift_word(word, shift)
            groups[key].append(word)

        return list(groups.values())


class Solution2:
    def shift_letter(self, letter, shift):
        # Handle non-alphabetic characters and ensure lowercase
        if not letter.isalpha():
            return letter
        
        base = ord('a')
        position_in_alphabet = ord(letter.lower()) - base
        new_position = (position_in_alphabet + shift) % 26
        return chr(base + new_position)
    
    def shift_word(self, word, shift):
        return ''.join(self.shift_letter(letter, shift) for letter in word)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strings:
            if not word:  # Handle empty strings
                key = ""
            else:
                # Calculate shift to make first character 'a'
                shift = ord('a') - ord(word[0].lower())
                key = self.shift_word(word, shift)
            groups[key].append(word)

        return list(groups.values())

if __name__ == "__main__":
    # Test cases
    sol = Solution()
    sol2 = Solution2()
    print(sol.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
    # Expected: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    print(sol2.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))

    print(sol.groupStrings(["a"]))
    # Expected: [["a"]]
    print(sol2.groupStrings(["a"]))

    print(sol.groupStrings(["abc", "bcd", "xyz", "ab", "bc"]))
    # Expected: [["ab","bc"],["abc","bcd","xyz"]]
    print(sol2.groupStrings(["abc", "bcd", "xyz", "ab", "bc"]))
