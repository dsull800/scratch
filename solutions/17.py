class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {2: 'abc', 3: 'def',
                        4: 'ghi', 5: 'jkl',
                        6: 'mno', 7 :'pqrs',
                        8: 'tuv', 9: 'wxyz'}

        if not len(digits):
            return []

        digit = digits[0]
        letters = digits_map[int(digit)]
        if digits[1:]:
            next_stuff = self.letterCombinations(digits[1:])
        else:
            return list(letters)

        output = []
        for letter in letters:
            out = [letter + ret_str for ret_str in next_stuff]
            output.extend(out)

        return output
