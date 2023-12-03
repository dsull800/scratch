class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        new_nums = [float('-inf')] + nums + [float('-inf')]
        del nums

        def binary_search(nums):
            mid = len(nums) // 2

            if len(nums) <= 2:
                return None
            elif nums[mid] == float('-inf'):
                return None
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid - 1
            elif nums[mid] < nums[mid + 1]:
                return mid + binary_search(nums[mid:])

            elif nums[mid] < nums[mid - 1]:
                return binary_search(nums[:mid + 1])

        return binary_search(new_nums)

