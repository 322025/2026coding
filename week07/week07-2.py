#week07-2.py 學習計畫
#LeetCode 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for a in asteroids:
            if a>0:#正的往右,不會跟左邊相撞
                ans.append(a)#直接塞
            else:#負的往左,可能會跟ans裡的東西相撞
                while ans and ans[-1]>0:
                    if abs(ans[-1])==abs(a):#絕對值大小都相同都消滅
                        ans.pop()#消滅
                        a=0
                        break#離開迴圈
                    elif abs(ans[-1])>abs(a):#右邊的比較小消滅右邊
                        a=0#消滅右邊
                        break
                    else:#左邊的比較小消滅左邊
                        ans.pop()
                if a!=0:ans.append(a)
        return ans
