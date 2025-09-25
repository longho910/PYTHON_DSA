from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # Include nums[i]
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # Skip nums[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


# ---- Test Case ----
nums = [2, 3, 6, 7]
target = 7

solution = Solution()
result = solution.combinationSum(nums, target)

print("Input:", nums, "Target:", target)
print("Output:", result)
