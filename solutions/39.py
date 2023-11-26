class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def get_combo_sums(candidates, target, combos):
            if target == 0:
                set_combos = Counter(combos)
                if set_combos not in res:
                    res.append(set_combos)
                return
            if target <= 0:
                return
            for i in candidates:
                get_combo_sums(candidates, target - i, combos + [i])

        get_combo_sums(candidates, target, [])
        return [reduce(lambda x, y: x+y, [[val]*count for (val, count) in sol.items()]) for sol in res]