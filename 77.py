class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        for i in range(1, k + 1):
            globals()[f'k_{i}'] = i
        globals()[f'k_{k + 1}'] = n + 1
        n_array = list(range(1, n + 1))
        combos = []

        def recursive_combos(k_val):
            if k_val == 0:
                return
            tmp = globals()[f'k_{k_val}']
            for val in range(globals()[f'k_{k_val}'], globals()[f'k_{k_val + 1}']):
                globals()[f'k_{k_val}'] = val
                combo = [globals()[f'k_{i}'] for i in range(1, k + 1)]
                if len(combos) == 0:
                    combos.append(combo)
                elif combo != combos[-1]:
                    combos.append(combo)

                if val > tmp:
                    recursive_combos(k_val - 1)
                    if k_val - 1 != 0:
                        globals()[f'k_{k_val - 1}'] -= 1
            globals()[f'k_{k_val}'] = tmp + 1

        recursive_combos(k)
        return combos