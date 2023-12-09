class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap_prof = sorted(zip(capital, profits), key=lambda x: x[0])

        heap = []

        projects_finished = 0

        c_ind = 0

        while projects_finished < min(k, len(capital)):
            while c_ind < len(capital) and cap_prof[c_ind][0] <= w:
                heappush(heap, -cap_prof[c_ind][1])
                c_ind += 1
            if heap:
                w += -heappop(heap)
            projects_finished += 1

        return w
