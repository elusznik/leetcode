class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for char in magazine:
            dict[char] = dict.get(char, 0) + 1
        for char in ransomNote:
            if char not in dict or dict[char] == 0:
                return False
            dict[char] -= 1
        return True