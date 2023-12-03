class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2

        if len(nums) == 0:
            return 0
        elif nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return mid + self.searchInsert(nums[mid+1:], target) + 1
        elif target < nums[mid]:
            return self.searchInsert(nums[:mid], target)
        else:
            raise Exception('wth')