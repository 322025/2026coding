#week05-4.py 2026-03-25 珼驹肈
#2352. Equal Row and Column Pairs
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total=sum([sum(row) for row in grid])#场癬ㄓ
        presum=0
        for row in grid:#硋row矪瞶
            presum+=sum(row)#рrow俱︽秈ㄓ
            if presum==total-presum:#场=场
                return True
        presum=0
        for col in zip(*grid):#р锣竚痻皚硋矪瞶
            presum+=sum(col)
            if presum==total-presum:#オ场=场
                return True
        return False
