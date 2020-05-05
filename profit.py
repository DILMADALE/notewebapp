def profit(stack_profit):
    min_stack_profit = stack_profit[0]
    max_profit = 0
    for price in stack_profit:
        min_stack_profit = min(min_stack_profit,price)
        print('min ', min_stack_profit)
        comparison_profit = price - min_stack_profit
        print('comp ', comparison_profit)
        max_profit = max(max_profit,comparison_profit)
        print('max ', max_profit)
    return max_profit


print(profit([12,23,3,10]))
