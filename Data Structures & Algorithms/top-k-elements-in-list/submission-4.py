class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = Counter(nums)

        
        buckets = [[] for _ in range(n + 1)]

        for key, val in count.items():
            buckets[val].append(key)


        res = []

        for i in range(n, 0 , -1):
            
            for n in buckets[i]:
                res.append(n)

                if len(res) == k:
                    return res

        return res
