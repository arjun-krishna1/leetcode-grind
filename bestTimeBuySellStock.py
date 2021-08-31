'''
GIVEN
INPUT
    prices: array of ints
        pries[i] is the price of a given stock on the ith dy
        
OUTPUT
    maximum profit you can achieve from this transaction
        if no profit return 0
        
    choosing a single day to buy one stock, different day in the future to sell that stack

BRUTE FORCE
    max_profit = 0
    iterate through prices with i
        iterate through prices starting at one past i with j
            get profit by selling at j after buying at i
                update max_profit with maximum
    return max_profit
    
OPTIMIZATION O(N) time O(1) space
    we only want to buy stock on the lowest day up to this point
    min_price = prices[0]
    max_profit = 0
    iterate through prices as i
        update min_price as the lowest stock price so far
        
        update this stock price as the profit from the lowest stock price
        max_profit = maximum profit so far
    return max_profit

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # store the minimum stock price and maximum profit so far
        min_price = prices[0]
        max_profit = 0
        
        for i in range(len(prices)):
            # update minimum stock price if htis is a new minimum
            min_price = min(prices[i], min_price)
            
            # replace this stocks price with the profit we would get if
            # we had bought at the min price and sold here instead
            prices[i] -= min_price
            
            # update max_profit if this is a new maximum profit
            max_profit = max(prices[i], max_profit)
        
        # max_profit
        return max_profit
