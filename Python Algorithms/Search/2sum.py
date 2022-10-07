def sum_num(A, u):
    #mergesort(n)
    A.sort();
    i = 0
    j = len(A) - 1
    count = 0
    while i <= j:
        if A[i] > u: return False
        elif A[j] > u or A[i] + A[j] > u: j -= 1
        elif A[i] + A[j] == u: return (A[i], A[j])
        else: i += 1
    return False

print(sum_num([0,1,3,5,7,10], 5))
