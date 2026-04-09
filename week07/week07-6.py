#week07-6.py 學習計畫
#LeetCode649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue=deque(list(senate))
        banR,banD=0,0#目前被消滅的次數是0
        R,D=senate.count('R'),senate.count('D')#目前各有幾個人
        while queue:#只要還有人在排隊,就繼續進行
            now=queue.popleft()#左邊吐出個字母他要消滅敵對陣營
            if now=='R':
                if banR>0:#已經紀錄要消滅一個人
                    R-=1#馬上消滅一個人
                    banR-=1#用掉一個消滅的名額
                    continue#你一出現消滅
                else:#沒有被消滅
                    banD+=1
                    queue.append(now)#再到最右邊排隊
            else:#now=='D'
                if banD>0:
                    banD-=1
                    D-=1
                    #continue
                else:
                    banR+=1
                    queue.append(now)
            if R==0:return 'Dire'#把R消滅光,'D'就得勝
            if D==0:return 'Radiant'#把D消滅光,'R'就得勝
