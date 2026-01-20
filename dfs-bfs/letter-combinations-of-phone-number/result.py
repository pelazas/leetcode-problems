class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = [int(c) for c in digits]
        keyboard = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8:"tuv", 9:"wxyz"
        }
        result = []
        
        def dfs(curr_string, idx):
            if idx == len(nums):
                result.append(curr_string)
                return
            current_num = nums[idx]
            letters = keyboard[current_num]
            for letter in letters:
                dfs(curr_string+letter, idx+1)

        dfs("",0)
        return result
        
        