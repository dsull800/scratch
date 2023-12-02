class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        len_nums = len(nums)
        total = 0

        max_sub = nums[0]
        cur_sum = 0
        left_ind = 0

        for ind, n in enumerate(nums):
            total += n
            if cur_sum <= 0:
                cur_sum = 0
                left_ind = ind

            cur_sum += n
            if cur_sum > max_sub:
                best = (left_ind, ind)

            max_sub = max(max_sub, cur_sum)

        min_sub = -nums[0]
        cur_sum = 0
        left_ind = 0

        for ind, n in enumerate(nums):
            if cur_sum <= 0:
                cur_sum = 0
                left_ind = ind

            cur_sum -= n
            min_sub = max(min_sub, cur_sum)

        return max(max_sub, total + min_sub) if min_sub != -total else max_sub
