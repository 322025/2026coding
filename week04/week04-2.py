#week04-2.py學習計畫
#1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N=len(gain)#陣列長度
        ans=H=0#一開始的長度是0
        for i in range(N):#逐個加起來
            H+=gain[i]#現在增減的量
            ans=max(ans,H)#更新最高的答案
        return ans
