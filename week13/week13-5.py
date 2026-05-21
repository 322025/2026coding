# week13-5.py 學習計畫 Heap / Priority Queue 第3頁, 超難題的
# LeetCode 2542. Maximum Subsequence Score
# 挑 k 個 index, 讓 nums1 對應的 k 個數相加, 再來 min(nums2 對應 k 個數) 希望最大

from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 先把 nums1 跟 nums2 合併起來
        # ex. [1,3,3,2]
        #     [2,1,3,4]
        N = len(nums1) # 陣列的長度

        # 為了配合後續依 nums2 大到小排序，我們把 nums2 放前面：(nums2[i], nums1[i])
        a = [ (nums2[i], nums1[i]) for i in range(N) ] # 左右合併起來
        #print(a)
        #a.sort() # 試試看: 小到大排好
        #print(a)
        a.sort(reverse=True) # 大到小排好（依據 nums2 數值大到小排序）

        # 這裡的 heap 用來維護目前挑選的 k 個 nums1 的值
        heap = [a[i][1] for i in range(k)]
        heapify(heap) # 之後將小到大依序吐掉 nums1 的這些數,換加入新的n1,n2組
        total = sum(heap)

        # a[k-1][0] 代表目前這 k 個裡面，最小的 nums2
        ans = total * a[k-1][0] # 前k項的nums1 及對應最小的 nums2 相乘

        for i in range(k, len(nums2)): # 後面將加入的數
            n2, n1 = a[i] # 將加入的對應的數 (n2是nums2, n1是nums1)
            heappush(heap, n1) # 加1
            total += n1 - heappop(heap) # 加1、吐1 (把最小的 nums1 吐掉)
            ans = max(ans, total * n2) # 更新答案

        return ans
