class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pv={} #val:index
        for i, n in enumerate(nums):
            diff=target - n
            if diff in pv:
                return [pv[diff],i]  
            pv[n]=i
        