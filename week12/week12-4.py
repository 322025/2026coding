# week12-4.py 學習計畫 Graph - DFS 第3題，這是 Medium 題
# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# 有 N 個城市，有 N-1 條路，希望大家走到 0 都是正向，有幾條路「出錯」？
# 解法：從 0 出發，全部走過，路不對，就 ans += 1

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set() # 走過的，不要再走
        path = defaultdict(list) # path[now] 與哪些城市相接

        for a, b in connections:
            # 建立雙向連接，但標記方向
            # (b, +1) 表示 a -> b 是原始方向（離開 0 的方向，出錯了）
            # (a, -1) 表示 b -> a 是反向（朝向 0 的方向，正確）
            path[a].append( (b, +1) )
            path[b].append( (a, -1) )

        def helper(now):
            ans = 0 # 有幾條路「方向不對」
            visited.add(now)

            for k, d in path[now]: # 城市 now 可以到城市 k, 方向是 d
                if k not in visited:
                    # 如果方向 d 是 +1，表示這條路是從 0 往外指的，需要反轉
                    if d == +1:
                        ans += 1 # 要檢測方向，若方向「出錯」+1
                    ans += helper(k) # 函式呼叫函式，裡面含有幾條「出錯」
            return ans

        return helper(0) # 從 0 出發
