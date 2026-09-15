class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        frequency_map = {}

        for i in nums:
            frequency_map[i] = frequency_map.get(i, 0) + 1

        for n in frequency_map:
            buckets[frequency_map[n]].append(n)

        result = []
        for item in reversed(buckets):
            for element in item:
                result.append(element)
                if len(result) == k:
                    return result
                

        
        

        
