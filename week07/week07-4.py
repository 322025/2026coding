#week07-4.py學習計畫
#LeetCode 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]#利用stack處理方括號及對應的數字
        nowN,nowS=0,''#左邊nowN數字 v.s右邊nowS字串
        for c in s:
            if c.isdigit():#若是數字就用十進位組合起來
                nowN=nowN*10+int(c)
            elif c.isalpha():#如果是數字就讓字串變長
                nowS+=c
            elif c=='[':#上括號:數字、字串放入stack
                stack.append((nowN,nowS))
                nowN,nowS=0,''#一組新的數字、字串
            elif c==']':#下括號:數字、字串放入stack
                prevN,prevS=stack.pop()
                nowS=prevS+prevN*nowS#重複的次數*字串
        return nowS
