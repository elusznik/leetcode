class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[list("aeiouyAEIOUY")]
        s=list(s)
        s_vowels=[]
        for char in s:
            if char in vowels:
                s_vowels.append(char)
                