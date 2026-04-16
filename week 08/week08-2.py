# week08-2.py 學習計畫 Binary Search 第1題
# LeetCode 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 另一種解法
        # for i in range(n+1):print(guess(i), end=' ')
        return bisect_left(range(n+1),0,key=lambda x:-guess(x))
        #for i in range(1,n+1):
        #   if guess(i)==0: return i
        # 不能用上面的FOR 迴圈，因為N有20億這麼大，試不完
        left,right = 1,n+1 #左右的範圍
        while left<right: # 左右的範圍還沒有[撞在一起]
           mid = (left + right) //2 # [猜]中間的數字
           if guess(mid)==0: return mid # 猜到中間的數字
           if guess(mid)>0: left =mid+1 # [暗示你]再高一點
           else:right=mid
        return left
