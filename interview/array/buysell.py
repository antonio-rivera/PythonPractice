def mini(e1, e2, idx):
    if e1 <= e2:
        return (e1, idx)
    else:
        return (e2, idx+1) 

def maxi(e1, e2, idx):
    if e1 >= e2:
        return (e1, idx)
    else:
        return (e2, idx+1) 

def maxProfit(prices: list[int]) -> int:
    profit = 0
    i = 0
    buy = True
    total_profits = []
    while(i < len(prices)-1):
        if buy:
            bought, idx = mini(prices[i], prices[i+1], i)
            profit -= bought
            i = idx
            buy = False
        else:
            selled, idx = maxi(prices[i], prices[i+1], i)
            profit += selled
            i = idx
            total_profits.append(profit)
            buy = True
        
        # i += 1
    if total_profits:
        profits = max(total_profits)
        if profits > 0:
            return profits
        return 0
    return 0
        

# def maxProfit(prices: list[int]) -> int:
#     profit = 0
    


prices = [6,1,3,2,4,7]
print(maxProfit(prices))