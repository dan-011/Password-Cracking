def champaign_sort(L):
    n = len(L)
    beginning = 0
    end = 0
    for j in range(n-2):
        if j%2 == 0:
            for i in range(beginning, n-end-1):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
            end += 1
        else:
            for i in range(n-end-1, beginning, -1):            
                if L[i-1] > L[i]:
                    L[i], L[i-1] = L[i-1], L[i]
            beginning += 1
def get_index_iter(L, item, left = None, right = None):
    if right is None:
        right = len(L)
        left = 0
    while right-left > 0:
        median = (left + right)//2
        if item < L[median]:
            right = median
        else:
            left = median + 1
    return left
# print(get_index_iter([1,2,3,4,5], 3.5))


# change left and right
def opt_insertion_sort(L):
    n = len(L)
    left = n-1
    right = n
    for i in range(1,n):
        item = L[n-1-i]
        index = get_index_iter(L, item, left, right) - 1
        #print("index = {}, beginning = {}".format(index, n-i-1))
        for j in range(n-1-i, index):
            L[j] = L[j+1]
        L[index] = item
        left -= 1


if __name__ == '__main__':
    import random
    n = 100

    # champaign_sort test
    L = [random.randint(0,100) for i in range(n)]
    L.append(-1)
    champaign_sort(L)
    assert L == sorted(L)

    # opt_insertion_sort test
    L = [random.randint(0,100) for i in range(n)]
    L.append(-1)
    L = [-3,3,2,-1,5,6,2,1,-2]
    opt_insertion_sort(L)
    assert L == sorted(L)
