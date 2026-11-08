class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        current=0
        for g in gain:
            current+=g
            alt=max(alt,current)
        return alt