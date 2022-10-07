def isSorted(stack):
    for i in range(len(stack)-1):
        if stack[i] > stack[i+1]:
            return False
    return True
def pancake(stack):
    for i in range(len(stack)-1, 0,-1):
        maxi = 0
        max = stack[0]
        for j in range(i+1):
            if max < stack[j]:
                max = stack[j]
                maxi = j
        if i != maxi:
            flipper = stack[:maxi+1]
            flipper.reverse()
            stack[:maxi+1] = flipper
            flipper = stack[:i+1]
            flipper.reverse()
            stack[:i+1] = flipper
    return stack
print(pancake([9,1,5,2,7,8,3,6,4]))
