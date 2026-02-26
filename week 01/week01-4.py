# week01-4.py 學習計畫 Array/String 第3題
# LeetCodeclass 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 不要上傳
        ans = [] # 答案的True 和 False將塞在裡面
        best = max(candies) # 目前小朋友(最多有幾個糖)
        for candie in candies: # 逐一檢查，如果把extraCandies給小朋友
            if candie + extraCandies >= best : ans.append(True)
            else: ans.append(False) # 他會不會>= 最多的，依序塞入ans
        return ans
