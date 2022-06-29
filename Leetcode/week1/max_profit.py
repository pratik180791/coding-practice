import sys

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [2,4,1]
op = 5
# op =
from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = sys.maxsize
    profit = 0
    temp_profit = 0
    if not prices or len(prices) == 1:
        return 0
    for i, curr_price in enumerate(prices):
        current_max = max(0, temp_profit+curr_price)
        temp_profit = max(temp_profit, current_max+curr_price)
        if curr_price<min_price:
            print(curr_price, min_price)
            min_price = curr_price
        elif curr_price-min_price>profit:
            profit = curr_price-min_price
    print(temp_profit)
    print(profit)
    current_max = 0
    profit = 0
    for i in range(1, len(prices)):
        #profit = prices[i]-prices[i-1]
        current_max += prices[i] - prices[i - 1]
        current_max = max(0, current_max)
        profit = max(current_max, profit)
    print(profit)
maxProfit(prices)
