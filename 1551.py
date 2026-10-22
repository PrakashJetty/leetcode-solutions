class Solution:
    def minOperations(self, n: int) -> int:
        k = n//2 -1 if n % 2 == 0 else n//2
        ans = 0
        for i in range(0, k + 1):
            ans += ((2 * i) + 1) if n % 2 == 0 else (2 * i)
        return ans
