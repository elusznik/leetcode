class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len1,len2=len(word1),len(word2)
        for i in range(min(len1,len2)):
            result.append(word1[i])
            result.append(word2[i])
        return "".join(result)+word1[i+1:]+word2[i+1:]