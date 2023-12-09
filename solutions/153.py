class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        new_nums = [float('inf')] + nums + [float('inf')]
        def min_search(nums):
            mid = len(nums) // 2
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif (nums[0] if nums[0] != float('inf') else nums[1]) < nums[mid]:
                return min_search(nums[mid:])

            elif (nums[0] if nums[0] != float('inf') else nums[1]) > nums[mid]:
                return min_search(nums[:mid+1])

        return min_search(new_nums)