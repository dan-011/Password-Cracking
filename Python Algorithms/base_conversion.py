# Convert a number to a given base (integer less than 10)
# Return the answer as a string
# Recursive implementation required
def convert_to_base(number, base):
    if number == 0:
        return ""
    else:
        return convert_to_base(number//base, base) + str(number%base)

def f(n):
    a = 0
    b = 1
    for i in range(4, n+1):
        a = b
        b = a + (i-1)*(i-2)/2
    return b

def f2(n):
    if n == 3:
        return 1
    else:
        return f2(n-1) + (n-1)*(n-2)/2
def recrfac(n):
    if n == 0:
        return 1
    else:
        return n*recrfac(n-1)

def iterfac(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        a = b
        b = a*i
    return b

def reverse(string):
    if string == "":
        return ""
    else:
        pop = string[-1]
        return pop + reverse(string[:-1])
def iterreverse(string):
    n = len(string)
    build = ""
    for i in range(n-1,-1,-1):
        build += string[i]
    return build

def recrharmonic(n):
    if n == 0:
        return 0
    else:
        return (1/n) + recrharmonic(n-1)

def iterharmonic(n):
    a = 0
    b = 0
    for i in range(1,n+1):
        a = b
        b = a + 1/i
    return b


if __name__ == '__main__':
    assert(convert_to_base(15895, 7) == '64225')
    assert(convert_to_base(95736, 8) == '272770')
    
assert recrharmonic(5) == iterharmonic(5)

def recrfib(n):
    d = {}
    return _recrfib(n, d)
def _recrfib(n, d):
    if n in d:
        return d[n]
    else:
        if n == 0 or n == 1:
            d[n] = n
            return n
        else:
            d[n] = recrfib(n-1)+recrfib(n-2)
            return d[n]

def iterfib(n):
    a = 0
    b = 1
    for i in range(n):
        b = a + b
        a = b - a
    return a

for i in range(10):
    assert recrfib(i) == iterfib(i)

def recrBS(L, item):
    if len(L) == 0:
        return False
    middle_index = len(L)//2
    if L[middle_index] == item:
        return True
    elif item < L[middle_index]:
        return recrBS(L[:middle_index], item)
    elif item > L[middle_index]:
        return recrBS(L[middle_index+1:], item)

assert recrBS([1,2,3,4,5], 5)
assert not recrBS([1,2,3,4,5], 6)

def effBS(L, item, left = 0, right = None):
    if right is None:
        right = len(L)
    medium = (left+right)//2
    if right - left == 0:
        return False
    if right - left == 1:
        return L[left] == item
    elif L[medium] == item:
        return True
    elif L[medium] < item:
        return effBS(L, item, left, medium)
    else:
        return effBS(L, item, medium, right)

def iterBS(L, item):
    left = 0
    right = len(L)
    while right - left > 1:
        median = (right+left)//2
        if L[median] == item:
            return True
        elif item < L[median]:
            right = median
        else:
            left = median
    if right - left == 0: return False
    else:
        return L[left] == item

def bubblesort(L):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                is_sorted = False
def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n-1 and L[j] > L[j+1]:
            print(L)
            L[j], L[j+1] = L[j+1], L[j]
            j += 1
l = [5,4,3,2,1]
insertionsort(l)
print(l)

def recrFib(n, store = None):
    if store is None:
        store = {}
    if n in store:
        return store[n]
    elif n == 0 or n == 1:
        store[n] = n
        return n
    else:
        store[n] = recrFib(n - 1, store) + recrFib(n - 2, store)
        return store[n]

def iterFib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(10):
    assert iterFib(i) == recrFib(i)
print(recrfib(7))
def fib(k):
     if k in [0,1]: return k
     return fib(k-1) + fib(k-2)
print(fib(7))
print(iterFib(7))
print(recrFib(7))

def f(n):
    if n == 3:
        return 1
    else:
        return f(n-1) + ((n-1)*(n-2))/2

def fiter(n):
    a = 1
    for i in range(4,n+1):
        a = a + ((i-1)*(i-2))/2
    return a

print(f(7))
print(fiter(7))

def factorial(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a
def function(n):
    a = 1
    for i in range(4,n+1):
        a = a + (n-1)*(n-2)/2
    return a