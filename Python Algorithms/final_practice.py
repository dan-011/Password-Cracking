def total_steps(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return total_steps(n-1) + total_steps(n-2) + total_steps(n-3)
def total_steps(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return total_steps(n-1) + total_steps(n-2) + total_steps(n-3)
print(total_steps(10))

def tsdyn(n):
    d = [0, 1, 2, 4]
    for i in range(4, n+1):
        d.append(d[i-1]+d[i-2]+d[i-3])
    return d[n]
print(tsdyn(10))

# We’re looking at the price of a given stock over n consecutive days, numbered i = 1, 2, . . . , n.
# For each day i, we have a price p(i) per share for the stock on that day. (We’ll assume for
# simplicity that the price was fixed during each day.) We’d like to know: How should we choose a
# day i on which to buy the stock and a later day j > i on which to sell it, if we want to maximize
# the profit per share, p(j) − p(i)? (If there is no way to make money during the n days, we
# should conclude this instead.) In the solved exercise, we showed how to find the optimal pair of
# days i and j in time O(n log n). But, in fact, it’s possible to do better than this. Show how to find
# the optimal numbers i and j in time O(n).

def stocks(n):
    # 1 5 2 3 9 4
    max_diff = 0
    max_val = n[-1]
    max_elem_index = len(n) - 1
    i = max_elem_index
    j = max_elem_index
    for k in range(n-1, -1, -1):
        if n[k] > max_val:
            max_val = n[k]
            max_elem_index = k
        elif max_val - n[k] > max_diff:
            max_diff = max_val - n[k]
            i = k
            j = max_elem_index
    return i,j

def coins(n, c):
    table = []
    for i in range(n+1):
        table.append(i)
    for coin in c:
        for i in range(len(table)):
            if i >= coin:
                table[i] = 1+table[i-coin]
    return table[-1]
print(coins(7,[1,2,4]))