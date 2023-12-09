class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target):
            mid = len(nums) // 2

            if len(nums) == 0:
                return [-1, -1]
            elif nums[mid] == target:
                left = [-1, -1]
                right = [-1, -1]
                if mid - 1 >= 0 and nums[mid - 1] == target:
                    left = binary_search(nums[:mid], target)
                if mid + 1 < len(nums) and nums[mid + 1] == target:
                    right = binary_search(nums[mid + 1:], target)
                    right = [mid + r + 1 if r != -1 else -1 for r in right]
                ans = [mid if left[0] == -1 else left[0], right[1] if right[1] != -1 else mid]
                return ans

            elif nums[mid] < target:
                right = binary_search(nums[mid + 1:], target)
                return [mid + right[0] + 1 if right[0] != -1 else -1, mid + right[1] + 1 if right[0] != -1 else -1]
            elif nums[mid] > target:
                return binary_search(nums[:mid], target)

        return binary_search(nums, target)