class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a','e','i','o','u'])
        start=0
        end=k
        substring=0
        substring=sum(1 for i in s[:k] if i in vowels)
        max_substring=substring             
        for end in range(k,len(s)):
            max_substring=max(max_substring, substring)
            if max_substring==k:
                return k
            if s[start] in vowels:
                substring-=1
            if s[end] in vowels:
                substring+=1
            start+=1
        return max(max_substring, substring)