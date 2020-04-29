# https://www.hackerrank.com/challenges/icecream-parlor/problem

def whatFlavors(costs, money):
    cost_dict = {}
    for i, cost in enumerate(costs):
        if money - cost in cost_dict:
            return (cost_dict[money - cost] + 1 ,  i + 1)
        else:
            cost_dict[cost] = i
            
money = 6
costs = [1, 3, 4, 5, 6]
whatFlavors(costs, money)
