#week07-5.py學習計畫
#933. Number of Recent Calls
class RecentCounter:
    def __init__(self):#一開始物件的建構子
        self.queue=deque()#宣告一個物件裡用self找到的queue變數

    def ping(self, t: int) -> int:
        self.queue.append(t)#從右邊塞入一個數
        while self.queue[0] < t - 3000:#目前最左邊最古老的t超過範圍
            self.queue.popleft()#python的左邊吐掉
        return len(self.queue)
