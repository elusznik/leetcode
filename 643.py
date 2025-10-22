class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        end=k
        max_avg=sum(i for i in nums[:k])/k
        current_sum=sum(nums[:k])
        for end in range(k,len(nums)):
            max_avg=max(max_avg, current_sum/k)
            current_sum=current_sum-nums[start]+nums[end]
            start+=1
        return max(current_sum/k, max_avg)