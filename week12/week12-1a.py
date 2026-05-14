class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # week12-1a.py 學習計畫 Graph - DFS 第1題 Medium 題
        # 房間裡有鑰匙，可以再開新的房間。最後能開全部房間嗎？
        # DFS: Depth First Search 通常會利用 stack 或 function stack (函式呼叫函式
        # 我們利用 stack 裡面有待處理的房間，一開始房間 0 是開的
        stack = [0]
        # visited 有去過、處理過的房間，不要再進去了
        visited = set()
        # 已經掛號、等待處理，下次有拿到鑰匙，不要再放入 stack 喔
        visited.add(0)
        # 只要 stack 還有東西，就繼續處理
        while stack:
            # 吐出 1 個房間，現在要來處理
            now = stack.pop()
            # 把 room now 房間裡，所有的鑰匙 k，都拿來檢查
            for k in rooms[now]:
                # 鑰匙 k 對應的房間 k 看過了，別再檢查
                if k in visited:
                    continue
                # 如果走到這裡，代表沒走過、沒有待處理的房間 k
                stack.append(k) # 加入 stack 資料結構
                visited.add(k)  # 標記這個房間也待處理、其他人不要再排處理
        # 房間的數目，全部都參觀過了，成功
        return len(rooms) == len(visited)
