#week04-4a.py學習計畫(重寫week04-2.py)
#1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N=len(gain)#陣列長度
        ans=H=0#一開始的長度是0
        for gg in gain:#進階for迴圈寫法
            H+=gg#現在增減的量
            ans=max(ans,H)#更新最高的答案
        return ans
