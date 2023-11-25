class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        value_mapper = dict()
        answer = []
        for (a_i, b_i), val in zip(equations, values):
            value_mapper[a_i] = value_mapper.get(a_i, []) + [(b_i, val)]
            value_mapper[b_i] = value_mapper.get(b_i, []) + [(a_i, 1 / val)]

        def recursive_finder(a_i, target_denom, visited):
            if a_i in visited or not value_mapper.get(a_i, None):
                return
            visited.append(a_i)
            for denominator, val in value_mapper[a_i]:
                if denominator == target_denom:
                    return val
                else:
                    rec_val = recursive_finder(denominator, target_denom, visited)
                    if isinstance(rec_val, int) or isinstance(rec_val, float):
                        return val * rec_val

        for query in queries:
            visited = []
            query_value = recursive_finder(query[0], query[1], visited)
            answer.append(query_value if query_value is not None else -1)
        return answer



