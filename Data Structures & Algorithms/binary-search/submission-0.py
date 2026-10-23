class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1          # ❌ n was undefined
        while l <= h:                      # ❌ should be <= not <
            m = (l + h) // 2              # ❌ use // not /
            if nums[m] == target:          # ❌ m is an index, need nums[m]
                return m                   # ❌ return the index m, not nums[i+1]
            elif nums[m] > target:
                h = m - 1                 # ❌ should shrink h, not l+=1
            else:
                l = m + 1                 # ❌ should grow l, not h+=1
        return -1                          # target not found   