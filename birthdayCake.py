#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_height_count = [0,0]
    for c in ar:
    	if c > max_height_count[0]:
    		max_height_count = [c,1]
    	elif c == max_height_count[0]:
    		max_height_count[1] += 1
    return max_height_count[1]



n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
