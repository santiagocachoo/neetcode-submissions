class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        n = len(nums)

        for i in range(n):
            difference = target - nums[i]
            if difference in numbers:
                return [numbers[difference], i]
            else:
                numbers[nums[i]] = i


            
        