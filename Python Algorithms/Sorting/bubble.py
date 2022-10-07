def bubble_sort(L):
    for i in range(len(L)-1):
        is_sorted = True
        
        for j in range(len(L)-1-i):
            
            if L[j] > L[j+1]:
                is_sorted = False
                L[j], L[j+1] = L[j+1], L[j]
        
        if is_sorted:
            break