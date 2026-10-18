class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        candidates = set()
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter = counter + 1
                candidates.add(counter)
            else:
                candidates.add(counter)
                counter = 0
        return max(candidates)
        