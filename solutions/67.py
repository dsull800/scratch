class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        if len(b) > len(a):
            a, b = b, a
        b = (len(a) - len(b)) * '0' + b
        a = a[::-1]
        b = b[::-1]

        ans = ''

        for i in range(0, len(a)):
            b_val = int(b[i])

            a_val = int(a[i])

            if a_val == b_val:
                if a_val == 0:
                    if carry:
                        carry = False
                        ans = '1' + ans
                    else:
                        ans = '0' + ans
                else:
                    if carry:
                        ans = '1' + ans
                    else:
                        ans = '0' + ans

                    carry = True
            else:
                if carry:
                    ans = '0' + ans
                else:
                    ans = '1' + ans

        ans = '1' * int(carry) + ans

        return ans

