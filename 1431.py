class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=0
        res=[]
        for kid in candies:
            if kid>max:
                max=kid
        for i,kid in enumerate(candies):
            if kid+extraCandies>=max:
                candies[i]=True
            else:
                candies[i]=False
        return candies