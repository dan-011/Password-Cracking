def merge_plannings(p1, p2):
    i, j = 0, 0
    L = []
    max_wage = 0
    current_wage1 = 0
    current_wage2 = 0
    last_wage = 0
    while i < len(p1) and j < len(p2):
        if p1[i][0] < p2[j][0]:
            current_wage1 = p1[i][1]
            max_wage = max(current_wage1, current_wage2)
            if max_wage != last_wage:
                L.append((p1[i][0], max_wage))
                last_wage = max_wage
            i += 1
            
        else:
            current_wage2 = p2[j][1]
            max_wage = max(current_wage1, current_wage2)
            if max_wage != last_wage:
                L.append((p2[j][0], max_wage))
                last_wage = max_wage
            j += 1
    L[i+j:] = p1[i:] + p2[j:]
    return L

def optimal_planning(jobs, left = 0, right = None):
    if right is None:
        right = len(jobs)
    if len(jobs) == 0:
        return jobs
    elif right - left <= 1:
        print(left)
        start = jobs[left][0]
        end = jobs[left][1]
        wage = jobs[left][2]
        pair = [(start, wage), (end, 0)]
        return pair
    median = (right + left)//2
    
    left = optimal_planning(jobs, left, median)
    right = optimal_planning(jobs, median, right)

    optimal = merge_plannings(left, right)

    return optimal

if __name__ == '__main__':
    first_planning = [(2, 4), (5, 0), (6, 3), (10, 0)]
    second_planning = [(3, 5), (7, 0), (9, 2), (13, 0)]
    merged = [(2, 4), (3, 5), (7, 3), (10, 2), (13, 0)]
    res_merge = merge_plannings(first_planning, second_planning)
    assert(res_merge == merged)

    jobs_offers = [(2, 8, 3), (5, 7, 5)]
    optimal = [(2, 3), (5, 5), (7, 3), (8, 0)]
    res_planning = optimal_planning(jobs_offers)
    assert(res_planning == optimal)


# #first_planning = [(2,4),(4,0), (5,5), (7,0)]
# #second_planning = [(8,3),(9,0),(10,2),(13,0)]
# #merged = [(2,2),(5,1),(6,0)]
# #first_planning = [(2, 4), (5, 0), (6, 3), (10, 0)]
# #first_planning = [(1,10), (12,0)]
# #second_planning = [(3, 5), (7, 0), (9, 2), (13, 0)]
# #merged = [(2, 4), (3, 5), (7, 3), (10, 2), (13, 0)]
# #print(optimal_planning([(2, 7, 6), (4, 13, 2), (1, 5, 11), (4, 8, 3)]))
# first = [(2,6),(7,0)]
# second = [(4,2),(13,0)]
# merged1 = [(2,6),(7,2),(13,0)]
# #print(merge_plannings(first, second))

# third = [(1,11),(5,0)]
# fourth = [(4,3),(8,0)]
# merged2 = [(1,11),(5,8),(8,0)]
# #print(merge_plannings(third, fourth))

# merged3 = [(1,11),(5,6), (7,3),(8,2),(13,0)]

# merged1 = [(1,11),(2,0)]
# merged2 = [(3,6),(13,0)]
# want = [(1,11),(8,2),(13,0)]
#print(merge_plannings(merged2, merged1))
#print(optimal_planning([(2, 7, 6), (4, 13, 2), (1, 5, 11), (4, 8, 3)]))