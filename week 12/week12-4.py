# week12-4.py 學習計畫 Graph - DFS 第3題 Medium 題
# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        path = defaultdict(list)
        for a,b in connections:
            path[a].append((b,+1))
            path[b].append((a,-1))

        def hepler(now):
            ans = 0
            visited.add(now)
            for k, d in path[now]:
                if k not in visited:
                    if d==+1: ans += 1
                    ans += helper(k)
            return ans
        return helper(0)
