class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for ind, digit in enumerate(digits[::-1]):
            value = digit + carry
            if value >= 10:
                dig_val = value % 10
                digits[(len(digits) - 1) - ind] = dig_val
                carry = value // 10
            else:
                digits[(len(digits) - 1) - ind] = value
                carry = 0
                break



        if carry:
            digits = [carry] + digits

        return digits