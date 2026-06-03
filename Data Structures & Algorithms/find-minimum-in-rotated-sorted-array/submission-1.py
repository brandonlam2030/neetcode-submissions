class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = nums[0]

        while l <= r: 
            m = (l+r)//2

            value = nums[m]
            minimum = min(value,minimum)
            if value >= nums[0]:
                l = m+1
            else:
                r = m-1

        return minimum
