class Solution:
    import re
    from collections import deque
    from functools import reduce
    def calculate(self, s: str, parts=None) -> int:
        index = 0
        res = 0
        plus = True
        res_array = [res]
        first = False
        if parts is None:
            first = True
            s = s.replace(' ','')
            # print(s)
            parts = re.split(r'(\+)', s)
            parts = [re.split(r'(-)', part) for part in parts]
            parts = [re.split(r'(\()', part) for part in reduce(lambda x,y: x+y, parts)]
            parts = [re.split(r'(\))', part) for part in reduce(lambda x,y: x+y, parts)]
            parts = filter(lambda x: False if x == '' else True,reduce(lambda x,y: x+y, parts))
            parts = list(parts)
            # print(list(parts))
        while index < len(parts):
            token = parts[index]
            # print(token)
            if token in '+-':
                plus = plus == (True if token == '+' else False)
            elif token == '(':
                new_index, new_res = self.calculate(s=None, parts = list(parts)[index+1:])
                res = res + int(new_res) if plus else res - int(new_res)
                index = index + new_index
                plus = True
            elif token == ')':
                if not first:
                    return index+1, res
                else:
                    return res
            # elif token == ' ':
            #     pass
            else:
                res = res + int(token) if plus else res - int(token)
                plus = True

            # if res_array[-1] != res and first:
            #     res_array.append(res)
                # print(res_array)
            index += 1


        return res
