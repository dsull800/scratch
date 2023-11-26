class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def get_permutations(nums, comb):
            if len(nums) == 1:
                res.append(comb + nums)
            for ind, num in enumerate(nums):
                comb = comb + [num]
                get_permutations(nums[:ind]+nums[ind+1:],comb)
                comb.pop()

        get_permutations(nums, [])
        return res
