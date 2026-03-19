#week04-4c.py學習計畫(重寫week04-4b.py)
#3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H=Counter(nums)#很多很多格
        for nn in nums:#逐一檢查
            if nn%2==0 and H[nn]==1:#偶數只出現一次
                return nn
        return -1
