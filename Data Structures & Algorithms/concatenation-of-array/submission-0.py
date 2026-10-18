class Solution:
    def insertElements(self, nums: List[int], target: List[int]):
        for num in nums:
            target.append(num)

    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        for i in range(2): # solos se sopia dos veces al parecer
            self.insertElements(nums, ans)
        
        return ans
        