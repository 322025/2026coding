#week05-3.py 厩策璸礶
#1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter =Counter(arr)#参璸计瞷Ω计
        s=set()#ノㄓ瞷Ω计琌常縒礚
        for c in counter:#盢计硋ㄓ
            #print(c,cpunter[c])#计瞷碭Ω
            #counter[c]琌常縒礚
            if counter[c] in s:#Τ瞷筁ア毖
                return False
            s.add(counter[c])#瞷硂瞷Ω计s柑
        return True#繦獽肚
