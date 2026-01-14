class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # found_triplets = set()
        # for i in range(len(nums)):
        #     target = -nums[i]
        #     seen = set()
        #     for j in range(i+1, len(nums)):
        #         complement = target - nums[j]
        #         if complement in seen:
        #             found_triplets.add((nums[i], nums[j], complement))

        #         seen.add(nums[j])
        
        # return [list(triplet) for triplet in found_triplets]

        # TWO POINTER APPROACH
        nums.sort()
        found_triplets = set()

        for i in range(len(nums)-1):
            l = i+1
            r = len(nums)-1
            
            while l != r:
                op_result = nums[i] + nums[l] + nums[r]
                if op_result == 0:
                    found_triplets.add((nums[i], nums[l], nums[r]))
                    l +=1
                elif op_result < 0:
                    l+=1
                elif op_result > 0:
                    r-=1

        return [list(triplet) for triplet in found_triplets]    
                

        