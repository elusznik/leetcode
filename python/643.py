class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        max_sum=current_sum=sum(nums[:k])
        len_nums=len(nums)
        for end in range(k,len_nums):
            current_sum=current_sum-nums[start]+nums[end]
            start+=1
            max_sum=max(max_sum, current_sum)
        return max_sum/k