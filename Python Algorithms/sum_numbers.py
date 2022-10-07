# [1, 2, 3, 4, 5, 6] 8

def mergesort(L):
    if len(L) <= 1:
        return L

    median = len(L)//2

    left = L[:median]
    right = L[median:]

    left = mergesort(left)
    right = mergesort(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        else:
            L[i+j] = right[j]
            j += 1
    L[i+j:] = left[i:] + right[j:]
    
    return L
def binary_search(n, L):
    left = 0
    right = len(L) - 1
    while left < right:
        median = (left + right)//2
        if n < L[median]:
            right = median
        elif n > L[median]:
            left = median
        else:
            return True
    return False
def sum_numbers_bs(u, A):
    A = mergesort(A)
    for i in A:
        search = u - i
        if search == 0 or binary_search(search, A):
            return (True, i, search)
    return False

def sum_numbers_bf(u, A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            if A[i] + A[j] == u:
                return (True, A[i], A[j])
    return False

def transfer(fName):
    a = []
    with open(fName) as f:
        for n in f:
            a.append(int(n))
    return a
a = transfer("listNumbers-10")
print(a)
print(sum_numbers_bs(116, a))