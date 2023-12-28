class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        sol_dict = {}
        str_append = ''
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                # y = mx + b
                if points[i][0] == points[j][0]:
                    m = float('inf')
                    str_append = str(points[j][0])
                else:
                    m = round((points[i][1] - points[j][1]) / (points[i][0] - points[j][0]), 5)
                b =  round(points[i][1] - m * points[i][0], 5)
                print(m, b, i ,j)
                sol_dict[str_append+str(m)+str(b)] = sol_dict.get(str_append+str(m)+str(b), set()).union(set([i, j]))
                str_append = ''
        print(sol_dict)
        return max([len(x) for x in sol_dict.values()])