# week12-5.py 學習計畫 Graph - DFS 第4題 Medium 題
# LeetCode 399. Evaluate Division
# 有很多分子、分母 的除法的關係

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        # 用 zip 把方程式和數值拉鏈起來同時處理
        for (a, b), v in zip(equations, values):
            path[a].append( (b, v) )   # 正著走：a/b = v
            path[b].append( (a, 1/v) ) # 倒著走：b/a = 1/v

        def helper(now, target, v0):
            # 如果變數不在資料庫裡，回傳 -1
            if now not in path or target not in path: return -1.0
            # 找到目標了，回傳累積的乘積
            if now == target: return v0

            visited.add(now)
            ans = -1.0
            for node, v in path[now]:
                if node not in visited: # 沒走過，就進去走走看、試試看
                    # 遞迴尋找，並將當前權重 v 乘上去
                    res = helper(node, target, v0 * v)
                    if res != -1.0: # 如果找到了解，就更新 ans
                        ans = res
                        break # 找到一個解即可停止
            return ans

        ans = []
        for a, b in queries:
            visited = set() # 每次查詢都要重新清空 visited
            ans.append( helper(a, b, 1.0) )

        return ans
