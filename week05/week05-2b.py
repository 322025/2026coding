#week05-2b.py厩策璸礶
#2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2=set(nums1),set(nums2)#材セ硂︽
        ans1=[]#nums1ぃnums2计
        for num in nums1:#硋
            if num not in nums2:#⊿柑
                ans1.append(num)#氮
        ans2=[]#nums2ぃnums1计
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return[list(set(ans1)),list(set(ans2))]#糶程年セ
