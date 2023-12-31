class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.nums = nums
        self.memo = [None] * len(nums)
        self.memo[-1] = self.nums[-1]
        self.memo[-2] = self.nums[-2]

        my_max = self.memo[-1]
        for i in range(-3, -len(nums) - 1, -1):
            self.memo[i] = max(self.nums[i] + my_max, self.memo[i + 1])
            my_max = max(self.memo[i + 1], my_max)
        return max(self.memo)
