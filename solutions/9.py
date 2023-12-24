class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        n_places = floor(log(x, 10))
        orig_x = x

        num_arr = []

        for place in range(n_places, -1, -1):
            rem = x // 10 ** place
            num_arr.append(rem)
            x -= rem * 10 ** place

        for i in range(0, len(num_arr)//2 + 1):
            if num_arr[i] != num_arr[(len(num_arr) - i) - 1]:
                return False
        return True