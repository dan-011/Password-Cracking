# def company_scheduling(supply, r, c):
#     schedule = ""
#     sums = [0]
#     schedules = [""]
#     for i in range(len(supply)):
#         if i < 3:
#             schedule += "A"
#             sums.append(r*supply[i] + sums[i])
#         else:
#             A = r*supply[i] + sums[i]
#             B = c*4 + sums[i-3]
#             if A < B:
#                 sums.append(A)
#                 schedule = schedules[i] + "A"
#             else:
#                 sums.append(B)
#                 schedule = schedules[i-3] + "BBBB"
#         schedules.append(schedule)
#     return schedules[-1]
# print(company_scheduling([11, 9, 9,12],1,10))

def company_scheduling(supply, r, c):
    sums = [0]
    for i in range(len(supply)):
        if i < 3:
            sums.append(r*supply[i] + sums[i])
        else:
            A = r*supply[i] + sums[i]
            B = c*4 + sums[i-3]
            if A < B:
                sums.append(A)
            else:
                sums.append(B)
    return sums[-1]
print(company_scheduling([11, 9, 9, 12],1,10))

def stocks(n):
    max_diff = 0
    max_elem = n[-1]
    max_elem_index = len(n) - 1
    for k in range(len(n)-1,-1,-1):
        if n[k] > max_elem:
            max_elem = n[k]
            max_elem_index = k
        else:
            if max_diff < max_elem - n[k]:
                max_diff = max_elem - n[k]
                j = max_elem_index
                i = k
    if max_diff == 0:
        return "Do not invest"
    else:
        return "Buy on day {} and sell on day {}".format(i+1, j+1)
