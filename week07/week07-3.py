#week07-3學習計畫
#2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for c in s:#逐一取出字母c在判斷
            if c=='*':ans.pop()#遇到*好吐掉一個字母
            else:ans.append(c)#把不是*的字母塞進去
        return''.join(ans)#用單單.join()把陣列join成字串
