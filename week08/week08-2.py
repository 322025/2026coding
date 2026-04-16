#week08-2 學習計畫 第一題
class Solution:
    def guessNumber(self, n: int) -> int:
# 方法 1：神奇的 bisect_left() 寫法，只要 1 行
#for i in range(n+1): print( -guess(i), end=' ' )  # 做個實驗，不用寫
#return bisect_left( range(n+1), 0, key=lambda x:-guess(x) )  # 一行抵下面 7 行
#for i in range(1, n+1):  # 「錯誤」的暴力法，for 迴圈找答案
#    if guess(i)==0: return i  # 猜中了，答案是 i
# 錯誤的方法 for 迴圈，不能用上面的 for 迴圈，因為 n 有 20 億這麼大，試不完
# 要用小學「猜數字」每次範圍猜一半，比它大、比它小，縮小範圍
# 方法 2: while left < right: 去逼近
        left, right = 1, n+1  # 左右的範圍 (|)
        while left < right:  # 左右的範圍還沒有「撞在一起」
            mid = (left + right) // 2  # (猜) 中間的數
            if guess(mid)==0: return mid  # 猜到中間的數字
            if guess(mid)>0: left = mid + 1 # (暗示你) 再高一點 (中點設成下界)
            else: right = mid  # (暗示你) 再低點 (中點設成上界)
        return left

