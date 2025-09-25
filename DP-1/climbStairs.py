class Solution:
    # Time: O(2^n), Space: O(N)
    def climbStairsRecursion(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)

    # Time: O(N), Space: O(N)
    def climbStairsTopDown(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)

    # Time: O(N), Space: O(N)
    def climbStairsBottomUp(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Time: O(N), Space: O(1)
    def climbStairsMostOptimized(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one


solution = Solution()
print(solution.climbStairsRecursion(20))
print(solution.climbStairsTopDown(20))
print(solution.climbStairsBottomUp(20))
print(solution.climbStairsMostOptimized(20))
