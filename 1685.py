class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i, num in enumerate(nums):
            result[0] += abs(nums[0] - nums[i])
        print(result[0])
        for i, num in enumerate(nums):
            if i != 0:
                result[i] = result[i -1] + (2 * (i -1) + 2  - n) * (nums[i] - nums[i -1])
        return result
