def selection_sort(L):
    n = len(L)
    # Repeat n -1 times to guarantee list is sorted
    for i in range(n-1):
        # Select: find the next biggest item
        big = 0
        for j in range(1, n-i):
            if L[j] > L[big]: big = j
        
        # Sort: put the next biggest item in its place
        L[n-1-i], L[big] = L[big], L[n-1-i]