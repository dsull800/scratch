class Solution:
    def __init__(self):
        self.course_mapper = dict()
        self.courses_left = None
        self.solution = []
        self.num_visited = 0

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.courses_left = set([i for i in range(0, numCourses)])
        for [a_i, b_i] in prerequisites:
            self.course_mapper[b_i] = self.course_mapper.get(b_i, []) + [a_i]

        def dfs(val, visited_so_far):
            visited_so_far = visited_so_far + [val]
            self.num_visited += 1
            self.courses_left = self.courses_left.difference(set([val]))
            for neighbor in self.course_mapper.get(val, []):
                cycle = False
                if neighbor in self.courses_left:
                    self.courses_left = self.courses_left.difference(set([neighbor]))
                    cycle = dfs(neighbor, visited_so_far)
                if cycle or neighbor in visited_so_far:
                    return True

            self.solution = [val] + self.solution

        for i in self.courses_left:
            if i not in self.courses_left:
                continue
            cycle = dfs(i, [])
            if cycle:
                return []

        return self.solution





