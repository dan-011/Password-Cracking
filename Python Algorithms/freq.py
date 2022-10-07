# def count_freq(item, list):
#     counter = 0
#     for i in list:
#         if i == item:
#             counter += 1
#     return counter
# def majority_elem(L):
#     if len(L) == 1:
#         return L[0]
#     median = len(L)//2
#     left_maj = majority_elem(L[:median])
#     right_maj = majority_elem(L[median:])
#     if left_maj == right_maj:
#         return left_maj
#     else:
#         left_count = count_freq(left_maj, L)
#         right_count = count_freq(right_maj, L)
#         if left_count > right_count: return left_maj
#         else: return right_maj

def count_freq(item, L, left, right):
    counter = 0
    for i in range(left,right):
        if L[i] == item: counter += 1
    return counter
def majority_elem(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        return L[left]
    median = (left + right)//2
    left_maj = majority_elem(L, left, median)
    right_maj = majority_elem(L, median, right)

    if left_maj == right_maj:
        return left_maj
    else:
        left_freq = count_freq(left_maj, L, left, right)
        right_freq = count_freq(right_maj, L, left, right)
        if left_freq > right_freq:
            return left_freq
        else:
            return right_freq
# def peak_elem(L):
# 	if len(L) == 1:
# 		return L[0]
# 	elif len(L) == 2:
# 		if L[0] > L[1]:
# 			return L[0]
# 		else:
# 			return L[1]
# 	else:
# 		median = len(L)//2
# 		if L[median] < L[median+1]:
# 			return peak_elem(L[median+1:])
# 		elif L[median] < L[median-1]:
# 			return peak_elem(L[:median])
# 		else:
# 			return L[median]

def peak_elem(L, left = None, right = None):
    if left is None:
        left = 0
        right = len(L)
    if right - left == 1:
        return L[left]
    elif right - left == 2:
        return max(L[left],L[left+1])
    else:
        median = (left + right)//2
        if L[median] < L[median+1]:
            return peak_elem(L, median+1, right)
        elif L[median] < L[median-1]:
            return peak_elem(L, left, median-1)
        else:
            return L[median]
assert peak_elem([1,2,6]) == 6
assert majority_elem([1,3,1,3,1,3,1]) == 1

