def find_min(L, m = 1, left = None, right = None):
    if right is None:
        left = 0
        right = len(L)-1

    median = (left + right)//2
    if right - left <= 1:
        return min(L[left], L[right])
    
    if L[median] < L[median+1]:
        return find_min(L, m, left, median)
    elif L[median] > L[median+1]:
        return find_min(L, m, median+1, right)
    else:
        index = 1
        while index <= m:
            if index + median >= len(L):
                return find_min(L, m, left, len(L)-m)
            elif L[index+median] == L[median]:
                index += 1
            elif L[index+median] < L[median]:
                return find_min(L, m, median+1, right)
            elif L[index+median] > L[median]:
                return find_min(L, m, left, median)


if __name__ == "__main__":
    L = [8,4,3,1,2,2,2,5,5]
    assert find_min(L, 3) == 1

    L = [5,5,5,1,3]
    assert find_min(L, 3) == 1

    L = [2,1,5,5,5,5]
    assert find_min(L, 4) == 1

    L = [5,2,2,2,1,3,4,8]
    assert find_min(L, 3) == 1

    L = [1,2,3,4,5,5]
    assert find_min(L, 2) == 1

    L = [5,4,3,3,3,2,1]
    assert find_min(L, 3) == 1

