import math
import matplotlib.pyplot as plt
from operator import itemgetter
def calcDemand(price, other_price):
    return math.exp(5 - 0.5*price)/(1 + math.exp(5 - 0.5*price) + math.exp(5 - 0.5*other_price))

#TODO Replace with new predicted marginal cost
mc = 1.8
other_prices = []
our_prices = []
profits = []
other_profits = []

#Loop used to generate equilibrium
for i in range(2000):
    other_price = i/200.0
    max_profit = -1
    max_price = other_price
    for j in range(3000):
        price = j/200.0
        profit = calcDemand(price, other_price) * (price - mc)
        if profit > max_profit:
            max_profit = profit
            max_price = price
    other_profit = calcDemand(other_price, max_price) * (other_price - mc)
    other_prices.append(other_price)
    our_prices.append(max_price)
    profits.append(max_profit)
    other_profits.append(other_profit)
    # print(max_profit, max_price, other_price, other_profit)
    if other_price == max_price:
        print(max_price)


optimum = []
optimum_other = []
maxPrice = -1
index = -1
#loop used to double check equilibrium results
for j in range(2000):
    other_price = j/200.0
    price = 5.6 #TODO replace with new optimal price to check
    profit = calcDemand(price, other_price) * (price - mc)
    other_profit = calcDemand(other_price, price) * (other_price - mc)
    optimum.append(profit)
    optimum_other.append(other_profit)
index, element = max(enumerate(optimum_other), key=itemgetter(1))
print(index/200.0, element)

x = []
for i in range(10):
    x.append(i)

# plt.plot(other_prices,our_prices, label = 'price')
plt.plot(other_prices, profits, label = 'optimum profit')
plt.plot(other_prices, other_profits, label = 'optimum other profit')
plt.plot(other_prices, optimum, label = 'our profit') #profit given our strat
plt.plot(other_prices, optimum_other, label = 'other profit given our') #other profit give our strat
# plt.plot(x, x) # y=x line
plt.legend()
plt.show()
