import sys

def getMinHoseDistance():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    content[1:-2] = sorted(content[1:-2])

    num_houses = content[0]
    house_addresses = []
    for i in range(1, len(content) - 1):
        house_addresses.append(content[i])
    num_hydrants = content[-1]
    if num_hydrants >= num_houses:
        return 0

    # tmp_hydrants = num_hydrants
    min_hydrants = []
    hi = 1000000
    lo = 0
    mid = 0
    while lo < hi:
        mid = int((lo + hi) / 2)
        
        hydrant_count = getMinHydrants(house_addresses, mid)
        if hydrant_count > num_hydrants:
            lo = mid + 1
        else:
            hi = mid
    
    return mid / 2


# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False

#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1

#     return found

# @param house_addresses : array of house distances
# @param D               : # of hydrants
# @return minimum number of hydrants necessary to cover houses
def getMinHydrants(house_addresses, D):
    count = 1
    # print D
    curr_hydrant = 0
    section_begin = house_addresses[0]
    for home in house_addresses:
        # print i
        if (home - section_begin) > D:
            count += 1
            section_begin = home
    return count

print "Distance is: %d" % getMinHoseDistance()

