# this method finds the smallest integer less than or equal to 
numlist = [0, 1, 10, 15, 21, 40, 41, 47, 49, 54, 65, 71, 79, 85, 100, 102, 200]

def found_item(num, numlist, index):
	is_good_left = index > 0 and numlist[index - 1] <= num
	if_good_right = index < len(numlist) - 1 and numlist[index] + 1 > num
	return is_good_left and is_good_left

def get_smallest_in_array_for_int(num, numlist):
	hi = len(numlist) - 1
	lo = 0
	mid = 0
	while lo < hi:
		mid = int((lo + hi) / 2)
		if found_item(num, numlist, mid):
			return mid
		elif num <= numlist[mid]:
			hi = mid - 1
		else:
			lo = mid + 1
	return mid

for n in range(250):
	ans = get_smallest_in_array_for_int(n, numlist)
	if not found_item(n, numlist, ans):
		print(n, numlist[ans])
	print(n,ans)