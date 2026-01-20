class Solution:
    def maxArea(self, height: List[int]) -> int:
        #area = min(height[i], height[j]) * (j-i)
        left = 0
        right = len(height) -1
        max_area = 0

        while right > left:
            current_area = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, current_area)

            # move pointer to shortest
            if height[left] > height[right]:
                right -=1
            else:
                left +=1

        return max_area


        