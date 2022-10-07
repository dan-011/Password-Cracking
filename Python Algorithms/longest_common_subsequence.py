def LCS(X, Y):
    m = len(X)
    n = len(Y)
    c = [[] for i in range(m+1)]
    for i in c:
        i += [0 for i in range(n+1)]  
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i][j-1],c[i-1][j])
    print(c)
    return c[m][n]


def fib_dyn(n):
    d = {}
    d[0] = 0
    d[1] = 1
    for i in range(2,n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]

def k_mult(x,y):
    if x < 10 and y < 10:
        return x*y
    else:
        m = len(str(x))
        n = len(str(y))
        half = max(m,n)//2
        a = x//(10**half)
        b = x%(10**half)
        c = y//(10**half)
        d = y%(10**half)
        a_c = k_mult(a,c)
        b_d = k_mult(b,d)
        ad_plus_bc = k_mult(a+b,c+d)-a_c-b_d
        return (a_c*(10**(2*half))) + (ad_plus_bc*(10**half)) + b_d

def find_rot(L, item, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right-left == 1:
        if item == L[left]:
            return left
        else:
            return -1
    else:
        med = (right + left)//2
        return max(find_rot(L, item, left, med),find_rot(L, item, med, right))
#  [8, 9, 10, 2, 5, 6] target = 10
def rot_search(L, item, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    print(L[left:right+1])
    if right - left == 1:
        if L[left] == item: return left
        else: return -1
    med = (right + left)//2
    print(L[med])
    if L[med] == item: return med
    elif L[med] < item and L[med+1] < item:
        return rot_search(L, item, left, med)
    #elif L[med] > item and :
    else:
        return rot_search(L, item, med+1, right)
# print(rot_search([8, 9, 10, 2, 3, 4, 5, 6, 7], 10))
def peak_entry(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        return L[left]
    elif right - left == 2:
        return max(L[left], L[left+1])
    else:
        med = (right + left)//2
        if L[med+1] > L[med]:
            return peak_entry(L, med+1, right)
        elif L[med-1] > L[med]:
            return peak_entry(L, left, med)
        else:
            return L[med]
def count_first(L, item, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        if L[left] == item:
            return left
        else:
            return 0
    med = (left + right)//2
    if item < L[med]:
        return count_first(L, item, left, med)
    elif L[med] == item:
        if med == left or L[med-1] != item: return med
        else:
            return count_first(L, item, left, med)
    else:
        return count_first(L, item, med+1, right)
def count_last(L, item, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        if L[left] == item:
            return left
        else:
            return 0
    med = (left + right)//2
    if item > L[med]:
        return count_last(L, item, med+1, right)
    elif L[med] == item:
        if med + 1 == right or L[med+1] != item: return med
        else: return count_last(L, item, med+1, right)
    else:
        return count_last(L, item, left, med)
def count_dups(L, item):
    return count_last(L, item) - count_first(L, item) + 1
print(count_dups([2, 5, 5, 5, 6, 6, 8, 8, 9, 9, 9], 8))
def smallest_missing_elem(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        if L[left] == left:
            return right
        else: return left
    med = (left+right)//2
    if L[med] == med:
        return smallest_missing_elem(L, med+1, right)
    else:
        return smallest_missing_elem(L, left, med)
print(smallest_missing_elem([0, 1, 2, 6, 9, 11, 15]))

def max_elem_array(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        return L[left]
    med = (left + right)//2
    left_max = max_elem_array(L, left, med)
    right_max = max_elem_array(L, med+1, right)
    if left_max == right_max:
        return left_max
    else:
        left_freq = 0
        right_freq = 0
        for i in range(left, right):
            if L[i] == left_max:
                left_freq += 1
            if L[i] == right_max:
                right_freq += 1
        if left_freq > right_freq:
            return left_max
        else:
            return right_max
print(max_elem_array([2,1,2,3,2,4,2]))

def max_sublist(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        return L[left]
    elif right-left < 1:
        return 0
    else:
        med = (left + right)//2
        left_max = max_sublist(L, left, med)
        right_max = max_sublist(L, med+1, right)
        left_cross = L[med]
        left_sum = 0
        right_cross = L[med+1]
        right_sum = 0
        for i in range(med+1, right):
            right_sum += L[i]
            right_cross = max(right_sum, right_cross)
        for i in range(med, left-1, -1):
            left_sum += L[i]
            left_cross = max(left_sum, left_cross)
        cross = left_cross + right_cross
        return max(left_max, cross, right_max)

print(max_sublist([-2,-5,6,-2,-3,1,6,-6]))

def search_offset_array(L, item, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        if L[left] == item:
            return left
        else: return None
    if right - left == 0: return None
    if right - left == 2:
        if L[left] == item:
            return left
        if L[left + 1] == item:
            return left+1
        else:
            return -1
    med = (left+right)//2
    if item < L[med]:
        return search_offset_array(L, item, left, med-1)
    elif item > L[med]:
        return search_offset_array(L, item, med+2, right)
    if item < L[med+1]:
        return search_offset_array(L, item, left, med)
    elif item > L[med+1]:
        return search_offset_array(L, item, med+3, right)
    elif L[med] == item:
        return med
    else:
        return med+1
print(search_offset_array([2, 1, 3, 5, 4, 7, 6, 8, 9],5))