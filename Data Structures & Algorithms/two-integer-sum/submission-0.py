from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = defaultdict()

        for i, n in enumerate(nums):
            temp = target - n
            print(i, n)

            if temp in dic:
                return [dic[temp], i]
            
            dic[n] = i

        return []
        