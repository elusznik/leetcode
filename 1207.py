class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict={}
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        if len(dict.values())!=len(set(dict.values())):
            return False
        return True