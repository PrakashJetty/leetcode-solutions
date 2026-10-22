class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        n = len(nums)
        m = len(l)
        ans = [False] * m
        for i in range(m):
            sub_list = nums[l[i]:r[i] + 1]
            sub_len = len(sub_list)
            sub_list.sort()
            diff = sub_list[1] - sub_list[0]
            ans[i] = True
            for j in range(1, sub_len):
                if sub_list[j] - sub_list[j - 1] != diff:
                    ans[i] = False
                    break;
            
        return ans
