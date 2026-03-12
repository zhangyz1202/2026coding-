# week03-4.py 學習計畫 Sliding Window 第3題
# LeetCode 1004. Max Consecutive Ones III
# 你可以把k個0翻轉變成1,那最長的一堆1,有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 # 一開始的蛇,肚子裡面沒有0
        N = len(nums) # 陣列長度N
        ans = 0 # 最長的、不會中毒而死的蛇，長度是多少呢
        tail = 0 # 尾吧一開始黏在0的位置，只有拉肚子才會往右縮
        for head in range(N):  # 蛇的頭，慢慢往右縮
            if nums[head]==0: # 吃到1個，[有毒的0]
                zeros +=1 # 身體內的毒素增加
                # if zeros>k:
                while zeros > k:
                    if nums[tail]==0:
                        zeros -= 1
                    tail += 1
            ans = max(ans,head-tail+1)
        return ans
