#week05-5學習計畫
#1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1=Counter(word1)
        counter2=Counter(word2)
        #用過的字母是否是相同的集合，左邊有右邊也會有
        if set(counter1.keys())!=set(counter2.keys()):#用的字母不同就失敗
            return False
        #把出現的次數小到大排好如果兩邊都一樣那就可以換到一樣為止
        if sorted(counter1.values())!=sorted(counter2.values()):#次數不同
            return False
        return True
