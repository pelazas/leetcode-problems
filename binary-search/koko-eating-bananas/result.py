class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best_solution = r

        while l <= r:
            k = (r + l) // 2
            hour_counter = 0
            for pile in piles:
                hour_counter += (pile // k) if pile % k == 0 else (pile // k + 1)
            if hour_counter > h:
                l = k +1
            else:
                best_solution = min(best_solution, k)
                r = k -1
        
        return best_solution