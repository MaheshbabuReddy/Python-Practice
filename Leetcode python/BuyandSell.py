class Solution(object):
    def maxProfit(self, prices):
        profit=0
        buy_stock=prices[0]

        for i in prices[1:]:
            if buy_stock > i   :
                buy_stock=i
            else:
                profit=max(profit,i-buy_stock)
                return profit
S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))