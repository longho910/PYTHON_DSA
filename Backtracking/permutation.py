from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur):
            # Base case: one full permutation found
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            # Explore choices
            for num in nums:
                if num in cur:  # skip if already used
                    continue
                cur.append(num)
                dfs(cur)
                cur.pop()  # backtrack

        dfs([])
        return res
      
solution = Solution()
res = solution.permute([1, 2, 3])
print(res)