def insertion_sort(L):
    n = len(L)
    
    # With insertion sort, have to repeat n times to gurantee list is sorted
    for i in range(n):
        
        # Bubble next "unsorted" item to its place in a
        # steadily growing sorted sublist at the end
        j = n-1-i
        while (j < n-1) and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1