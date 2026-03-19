#week04-4b.py學習計畫(重寫week04-3.py)
#3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H=[0]*200#很多很多格
        for nn in nums:#第一次處理
            H[nn]+=1#把出現的數字塞進H[]裡

        for nn in nums:#逐一檢查
            if nn%2==0 and H[nn]==1:#偶數只出現一次
                return nn
        return -1
