"""\
    6. Best Stock
    
       You are given the current stock prices. You have to find out which stocks
       cost more.

       Input: The dictionary where the market identifier code is a key and the
       value is a stock price.

       Output: A string and the market identifier code.
       
       Example:
       
           best_stock({
                       'CAC': 10.0,
                       'ATX': 390.2,
                       'WIG': 1.2
                       }) == 'ATX'
           
           best_stock({
                       'CAC': 91.1,
                       'ATX': 1.01,
                       'TASI': 120.9
                       }) == 'TASI'

       Preconditions: All the prices are unique.
"""

def best_stock(data):

    bestprice = 0
    beststock = ""
    
    for i in data.keys():
        if data[i] > bestprice:
            bestprice = data[i]
            beststock = i
            
    return beststock

print(best_stock({'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}))
print(best_stock({'CAC': 91.1, 'ATX': 1.01, 'TASI': 120.9}))
