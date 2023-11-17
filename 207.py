class Solution:
    def __init__(self):
        self.overall_visited = set()
        self.course_mapper = dict()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for [a_i, b_i] in prerequisites:
            self.course_mapper[b_i] = self.course_mapper.get(b_i, []) + [a_i]
            self.overall_visited = self.overall_visited.union(set([a_i, b_i]))

        def cycle_detector(a_i, visited):
            if a_i in visited:
                return True
            elif a_i not in self.overall_visited:
                return False
            elif self.course_mapper.get(a_i, None) is None:
                return False
            else:
                for course in self.course_mapper[a_i]:
                    self.overall_visited = self.overall_visited.difference(set([a_i]))
                    is_cycle = cycle_detector(course, visited + [a_i])
                    if is_cycle:
                        return is_cycle
                        break

        for course in self.overall_visited:
            visited = []
            if cycle_detector(course, visited):
                return False
        return True