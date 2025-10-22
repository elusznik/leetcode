class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(list("aeiou"))
        start=0
        end=k
        substring=0
        for i in range(start,end):
            if s[i] in vowels:
                substring+=1
        max_substring=substring             
        for end in range(k,len(s)):
            if substring>max_substring:
                max_substring=substring
            if max_substring==k:
                return k
            if s[start] in vowels:
                substring-=1
            if s[end] in vowels:
                substring+=1
            start+=1
        return max(max_substring, substring)