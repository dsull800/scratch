class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = None
        for row in range(0, len(matrix) - 1):
            if matrix[row][0] <= target < matrix[row + 1][0]:
                target_row = row
                break

        if target_row is None:
            if matrix[len(matrix) - 1][0] <= target <= matrix[len(matrix) - 1][-1]:
                target_row = len(matrix) - 1
            else:
                return False

        def binary_search(nums, target):
            mid = len(nums) // 2
            if len(nums) == 0:
                return False
            elif nums[mid] == target:
                return True
            elif nums[mid] > target:
                return binary_search(nums[:mid], target)
            elif nums[mid] < target:
                return binary_search(nums[mid + 1:], target)

        return binary_search(matrix[target_row], target)