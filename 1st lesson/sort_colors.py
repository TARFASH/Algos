from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(3):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums[last], nums[j] = nums[j], nums[last]
                    last += 1