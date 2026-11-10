class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = dict()
        for i,num in enumerate(nums):
            if(m.get(num) != None and (i - m[num]) <= k):
                return True
            m[num] = i
        return False

        