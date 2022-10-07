import random
from TimeFunctions import time_function


def find_missing_1(L):
    n = len(L)
    for i in range(n+1):
        if i not in L:
            return i

def find_missing_2(L):
    L.sort()
    test = 0
    for i in L:
        if i != test:
            return test
        test += 1
    return len(L)
    

def find_missing_3(L):
    n = len(L)
    sumk = (n*(n+1))/2
    sumList = 0
    for i in L:
        sumList += i
    return sumk - sumList

def find_missing_4(L):
    S = set(L)
    n = len(L)
    for i in range(n+1):
        if i not in S:
            return i


if __name__ == '__main__':
    # Create a randomized permutation with one element missing
    N = 100
    my_list = list(range(N + 1))
    random.seed()
    random.shuffle(my_list)
    item = my_list.pop()

    # Print the output
    print(find_missing_1(my_list))
    print(find_missing_2(my_list))
    print(find_missing_3(my_list))
    print(find_missing_4(my_list))

    #find_missing_1 Test
    assert find_missing_1(my_list) == item

    #find_missing_2 Test
    assert find_missing_2(my_list) == item

    #find_missing_3 Test
    assert find_missing_3(my_list) == item

    #find_missing_4 Test
    assert find_missing_4(my_list) == item