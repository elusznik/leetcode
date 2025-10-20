class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        pref=[]
        suff=[]
        for i,num in enumerate(nums):
            if i==0:
                pref.append(num)
            else:
                pref.append(pref[-1]*num)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suff.append(nums[i])
            else:
                suff.append(suff[-1]*nums[i])
        suff=suff[::-1]
        for i in range(len(nums)):
            if i==0:
                res.append(suff[i+1])
            elif i==len(nums)-1:
                res.append(pref[i-1])
            else:
                res.append(pref[i-1]*suff[i+1])
        return res