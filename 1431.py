class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        for i,kid in enumerate(candies):
            if kid+extraCandies>=maximum:
                candies[i]=True
            else:
                candies[i]=False
        return candies