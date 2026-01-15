class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_length = float('inf')
        counter = 0
        for r in range(len(nums)):
            counter += nums[r]

            while counter >= target:
                min_length = min(min_length, r-l+1)
                counter -= nums[l]
                l+=1
                
        return 0 if min_length == float('inf') else min_length

        