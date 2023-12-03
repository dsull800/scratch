class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > nums[-1]:
            new_nums = [float('inf')] + nums + [float('-inf')]
            def get_rotation(nums, target):
                mid = len(nums) // 2
                print(nums)
                if nums[mid-1] >= target >= nums[mid+1]:
                    if nums[mid] > nums[mid - 1]:
                        return mid + 1
                    return mid
                elif nums[mid] > target:
                    return mid + get_rotation(nums[mid:], target)
                elif nums[mid] < target:
                    return get_rotation(nums[:mid+1], target)
            rot = get_rotation(new_nums, nums[0])
            print(rot, new_nums[rot:-1] + new_nums[1:rot])
            real_nums =  new_nums[rot:-1] + new_nums[1:rot]
        else:
            real_nums = nums
            rot = 1

        def binary_search(nums, target):
            mid = len(nums) // 2
            if len(nums) == 0:
                return -1
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                res = binary_search(nums[mid+1:], target)
                return res if res == -1 else res + mid + 1
            elif nums[mid] > target:
                return binary_search(nums[:mid], target)

        res = binary_search(real_nums, target)
        return (res + rot - 1) % len(nums) if res != -1 else res
