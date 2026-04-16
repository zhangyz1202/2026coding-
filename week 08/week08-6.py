# week08-6.py 學習計畫 Binary Search 最難的第4題
# LeetCode 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total=0
        for pile in piles:
            total += pile // k
            if pile % k >0:total+=1
        return total <= h
    return bisect_left(range(1,max(piles)),True,key=helper)+1
