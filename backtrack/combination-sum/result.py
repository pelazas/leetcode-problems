class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        
        def backtrack(remaining, stack, start_index):
            if remaining == 0:
                solutions.append(list(stack))
                return
            if remaining <0:
                return
            for i in range(start_index, len(candidates)):
                stack.append(candidates[i])
                backtrack(remaining - candidates[i], stack, i)
                stack.pop()
        
        backtrack(target, [], 0)
        return solutions
        