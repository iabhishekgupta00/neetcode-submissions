class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n ,0)+1

        freq_sort = sorted(freq , key = freq.get , reverse = True)

        return freq_sort[:k]
        