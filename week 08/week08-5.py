# week08-5.py 學習計畫 Binary Search 第3題
# LeetCode 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N=len(nums)
        if N==1: return 0

        for i in range(N):
            if i ==0:
                if nums[i]>nums[i+1]: return i
            elif i==N-1:
                if nums[i]>nums[i-1]:return i

            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
