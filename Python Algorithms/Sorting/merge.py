def mergesort(L):
    # 1) Divide into subproblems
    # 2) Solve subproblems
    # 3) Combine solution to subproblems

    # Base case: list of 1 or 0 items is already sorted
    if len(L) <= 1: return L

    # otherwise: recursively split list in two until base case
    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    left = mergesort(left)
    right = mergesort(right)
    

    # left and right are sorted sublists. Zip 'em up.
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
    
        else:
            L[i+j] = right[j]
            j += 1
    
    # Add any remaining sublist items to L
    L[i+j:] = left[i:] + right[j:]    

    # L is the sorted version of this list at this level of recursion
    return L