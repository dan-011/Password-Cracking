def quicksort(L, left=0, right=None):
    if right is None: right = len(L)
    # Only run while sublist has len > 1
    if right - left <= 1: return None

    # Set up indices for pivoting 
    pivot = right - 1
    i, j = left, pivot - 1 # Our indices for looking through sublists
    
    # Pivot all items between left and right
    while i < j:
        while L[i] < L[pivot]: i += 1

        while i < j and L[j] >= L[pivot]: j -= 1

        if i < j: L[i], L[j] = L[j], L[i]
        
    # Swap pivot and i, if neccessary
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i

    quicksort(L, left, pivot)   # Recursivley call on left
    quicksort(L, pivot+1, right)# Recursively call on right