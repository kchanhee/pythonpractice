# Sample data coming in

# A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5
# A A A A A b b c c a


# What is the characterm was really long, and we had memory constraints


# Possible sampling results

# A sampled every 10 
# A b every 5
# A c every 5
import operator
import random
import bisect
import time

''' A bit brute force method, This will require some more memory but it is still constant.
    Extra time complexity comes from trying to find the bucket which has time up to 2 * O(62) extra time complexity since
    we search for the range of the random-number'''
# @param: stream - (list of chars)
# @param: rate - sampling rate string
freq_dict = {}
bucket = {}

def parse_str(stream, rate):
    if len(stream) < rate or len(stream) == 1:
        return stream[0]
    # freq_dict = {}
    stream = stream.split(' ')
    for i in stream:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    # freq_dict = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse = True)

    sample = ""
    # print freq_dict
    # generate the bucket based on frequency.
    generateBucket()
    '''pick random number from 0 to length of stream and see which bucket it falls into (range of buckets 
    determined via weight).'''
    ''' The length of the dictionary is finite MAX is 62 = (26 + 26) + 10 => # of upcase + # of downcase 
       + # of digits'''
    
    while len(sample) < (len(stream) / rate):
        rand_num = random.randint(0, len(stream))
        # print rand_num
        sample += lookupKey(rand_num)
    return sample

# Bucket creates a ((start,end), key) where (start, end) is the range(start,end)
def generateBucket():
    count = 0
    for k,v in freq_dict.items():
        bucket[(count, count+v)] = k
        count += v

def lookupKey(number):
    for (start,end), key in bucket.items():
        # print start, end
        if start <= number <= end:
            return key
        
stream = "A A A A A b b c c a"
stream1 = "A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5"
stream2 = "A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5"
stream3 = "A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5 A a 1 1 0 a a b a a 5 1 3 5 1 5 8 8 7 a 8 9 8 7 1 4 5"

rate = 10
rate1 = 5

start_time_brute = time.time()
sample1 = parse_str(stream, rate1)
sample1_time = time.time() - start_time_brute

freq_dict = {}
bucket = {}
start_time_brute = time.time()
sample2 = parse_str(stream1, rate1)
sample2_time = time.time() - start_time_brute

freq_dict = {}
bucket = {}
start_time_brute = time.time()
sample3 = parse_str(stream2, rate1)
sample3_time = time.time() - start_time_brute

freq_dict = {}
bucket = {}
start_time_brute = time.time()
sample4 = parse_str(stream3, rate1)
sample4_time = time.time() - start_time_brute



print 'Semi Brute Force'
print 'sample 1: ', sample1, ' runtime: ', sample1_time
print 'sample 2: ', sample2, ' runtime: ', sample2_time
print 'sample 3: ', sample3, ' runtime: ', sample3_time
print 'sample 4: ', sample4, ' runtime: ', sample4_time

print

# ------------------------------------------------------------------------------------------------ #
# A method that does preprocessing and returns a number corresponding to key based on weight
# Uses binary search to determine which key to use based on the the random number
# Time Complexity is O(N) + O(ln(N)) = O(N) * O(N/rate) (since we need to parse the string, O(log n) for search)
# Dictionary saves the frequency (weights) so at most we have 62 distinct keys (finite) O(1) - space complexity
# accessing a list/dictionary is O(1)
class WeightedRandomGenerator(object):
    def __init__(self, weights):
        self.cumulative_weights = []
        running_total = 0

        # iterate through all the weights and create the cumulative frequency
        for w in weights:
            running_total += w
            self.cumulative_weights.append(running_total)

    # Do binary search here
    def next(self):
        rnd = random.random() * self.cumulative_weights[-1]
        return bisect.bisect_left(self.cumulative_weights, rnd)

    def __call__(self):
        return self.next()

def parse_str_weighted(stream, rate):
    stream = stream.split(' ')
    if len(stream) < rate or len(stream) == 1:
        return stream[0]
    # freq_dict = {}
    for i in stream:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    # freq_dict = sorted(freq_dict.items(), key=operator.itemgetter(1), reverse = True)
    wrg = WeightedRandomGenerator(freq_dict.values())
    sample = ""
    x = []
    '''pick random number from 0 to length of stream and see which bucket it falls into (range of buckets 
    determined via weight). Then use binary search to grab the appropriate number'''
    ''' The length of the dictionary is finite MAX is 62 = (26 + 26) + 10 => # of upcase + # of downcase 
       + # of digits'''
    
    while len(sample) < (len(stream) / rate):
        key = freq_dict.keys()[wrg.next()]
        sample += key
        freq_dict[key] -= 1
        # sample += '1'
    return sample
        


rate = 10
rate1 = 5
start_time_eleg = time.time()
sample1 = parse_str_weighted(stream, rate1)
sample1_time = time.time() - start_time_eleg

freq_dict = {}
start_time_eleg = time.time()
sample2 = parse_str_weighted(stream1, rate1)
sample2_time = time.time() - start_time_eleg

freq_dict = {}
start_time_eleg = time.time()
sample3 = parse_str_weighted(stream2, rate1)
sample3_time = time.time() - start_time_eleg

freq_dict = {}
start_time_eleg = time.time()
sample4 = parse_str_weighted(stream3, rate1)
sample4_time = time.time() - start_time_eleg

print 'More Elegant Method'
print 'sample 1: ', sample1,' runtime: ', sample1_time
print 'sample 2: ', sample2,' runtime: ', sample2_time
print 'sample 3: ', sample3,' runtime: ', sample3_time
print 'sample 3: ', sample4,' runtime: ', sample4_time

# ------------------------------------------------------------------------------------------------ #
# Fibonacci using Memoization (DP) and Recursion

# fib_nums = {}
# def fib(n):
#     if n == 0:
#         return 0
#     if n in fib_nums:
#         return fib_nums[n]
#     else:
#         if n < 2:
#             fib_nums[n] = n
#         else:
#             fib_nums[n] = fib(n-2) + fib(n-1)
#         return fib_nums[n]

# n = 10
# fibs = fib(10)
# fib_list = fib_nums.values()
