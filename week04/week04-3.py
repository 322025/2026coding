#week04-3.py學習計畫
#3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans=-1#找不到答案會是-1
        N=len(nums)#有N個數字
        H=[0]*200#很多很多格
        for i in range(N):#第一次處理
            H[nums[i]]+=1#把出現的數字塞進H[]裡

        for i in range(N):#逐一檢查
            if nums[i]%2==0 and H[nums[i]]==1:#偶數只出現一次
                return nums[i]
        return -1
