# week07-4.py 學習計畫 Stack 第3題
# LeetCode 394. Decode String
# 將字串解碼 數字代表[重複的次數]會把右邊[方括號]裡的字串重複
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        nowN, nowS = 0,''
        for c in s:
            if c.isdigit():
                nowN=nowN*10+int(c)
            elif c.isalpha():
                nowS += c
            elif c=='[':
                stack.append((nowN,nowS))
                nowN,nowS=0,''
            elif c==']':
                prevN,prevS=stack.pop()
                nowS=prevS+prevN*nowS
        return nowS
