def toys(prices,balance):       # O(nlogn)
    prices.sort()
    t = 0
    for i in prices:
        balance -= i
        if balance < 0:
            return t
        t += 1
    return t



if __name__ == '__main__':
    K = 50
    cost = [1, 12, 5, 111, 200,
            1000, 10, 9, 12, 15]
    N = len(cost)
 
    print(toys(cost, K))