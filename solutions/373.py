class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for num1 in nums1[:k]:
            for num2 in nums2[:k]:
                heappush(heap, (num1+num2, (num1, num2)))

        return [pair[1] for pair in nsmallest(k, heap)]