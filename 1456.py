class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(list("aeiou"))
        start=0
        end=k
        substring=0
        max_substring=0
        for i in range(len(s)-k+1):
            for j in range(start,end):
                if s[j] in vowels:
                    substring+=1
            if substring>max_substring:
                max_substring=substring
            substring=0
            start+=1
            end+=1
        return max_substring