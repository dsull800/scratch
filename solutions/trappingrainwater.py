class Solution:
    def trap(self, height: List[int]) -> int:
        slow_pointer = 0
        fast_pointer = 1
        # middle_min = 0
        left_max = height[0]
        right_max = 0
        proposed_additions = []
        overall_addition = 0
        worder = []
        for index, h in enumerate(height):
            if index == 0:
                pass
            if h >= left_max:
                overall_addition += sum(proposed_additions)
                proposed_additions = []
                slow_pointer = index
                left_max = h
                worder.append(0)
                right_max = 0
            else:
                if h >= right_max:
                    fast_pointer=index
                    right_max = max(h, right_max)
                proposed_additions.append(left_max - h)
                worder.append(left_max - h)
            if h !=0:
                latest_non_zero = index
        if len(proposed_additions):
            print(proposed_additions)
            offset = fast_pointer - len(height)+1
            if offset + len(height) < latest_non_zero:
                offset = latest_non_zero
            if offset== 0:
                offset = len(proposed_additions)
            print(offset)
            print(fast_pointer)
            addition = sum(proposed_additions[:offset]) - (left_max - right_max) * len(proposed_additions[:offset])
            print(addition)
            overall_addition += addition
        print(height)
        print(worder)
        return overall_addition
