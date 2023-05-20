def spread(prices):
    spread = round(prices[0][0].get('keys')-prices[1][0].get('keys'),2)
    print("The spread is: ",spread)
    return spread
