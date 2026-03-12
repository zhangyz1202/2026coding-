# week03-3.py 學習計畫 Sliding Window 第1題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# 母音 Vowels: a,e,i,o,u,長度K的小字串,最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') # 把5個字母,變成set()
        # 以後用 if c in vowels: 就可以快速確認他是母音
        # 以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        count = 0 # 紀錄目前有幾個母音
        for i in range(k): #　找前面ｋ字母，逐一檢查，是不是母音
            if s[i] in vowels: count += 1 # 找到1個字母
        ans = count #　離開迴圈的，確認前ｋ個字母，有count 個母音
        N = len(s) # 全部字串長度 N
        for i in range(k,N): # 右邊的每個字母，逐一檢查
            if s[i] in vowels: count +=1
            if s[i-k] in vowels: count -=1
            ans = max(ans,count) #　更新答案
        return ans
