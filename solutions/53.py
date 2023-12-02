class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        best_pair = (left, right + 1)
        best = float('-inf')
        cur_sum = nums[0]
        while right < len(nums):
            if cur_sum >= best:
                best_pair = (left, right + 1)
                best = cur_sum
            if cur_sum >= 0:
                right += 1
                if right < len(nums):
                    cur_sum += nums[right]
            else:
                cur_sum -= nums[left]
                left += 1
                if left > right:
                    right += 1
                    if right < len(nums):
                        cur_sum += nums[right]

        return sum(nums[best_pair[0]:best_pair[1]])



