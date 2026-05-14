# week12-1a.py 學習計畫 Graph - DFS 第1題 Medium 題
# 房間裡有鑰匙，可以再開新的房間，最後能開全部房間嗎
# DFS : Depth First Search 通常利用 stack funvtion stack (函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while stack:
            now = stack.pop()
            for k in rooms[now]:
                if k in visited: continue
                stack.append(k)
                visited.add(k)
        return len(rooms) == len(visited)
