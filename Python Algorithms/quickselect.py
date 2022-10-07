def quickselect(L, left=0, right=None):
    
    # Initialize right on the first call
    if right is None: right = len(L)

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

    # Best case: we just found the pivot
    if pivot == (len(L)-1) // 2 : return L[pivot]
    
    elif pivot > (len(L)-1) // 2 : return quickselect(L, left, pivot)    # Recursivley call on left
    elif pivot < (len(L)-1) // 2 : return quickselect(L, pivot+1, right) # Recursively call on right