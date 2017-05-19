class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    	if sum(gas[k] - cost[k] for k in xrange(len(gas))) < 0:
    		return -1
    	curr_start_station = 0
    	while curr_start_station < len(gas):
    		gas_left = 0
    		for i in range(0, len(gas)):
    			# add the gas
    			gas_left += gas[(i + curr_start_station) % len(gas)] # since this is a circle
    			if gas_left < cost[(i + curr_start_station) % len(gas)]: # not enough gas to go to next station
    				# print "NOT ENOUGH GAS TRY STARTING FROM NEXT STATION"
    				curr_start_station += 1 # start at next station
    				i = 0
    				break
    			gas_left -= cost[(i + curr_start_station) % len(gas)] # subtract the cost of going to next
    			# print "gas_left: %d, start_station: %d" % (gas_left, curr_start_station)
    		if i == len(gas) - 1: # it successfully made it full circle return index of starting point
    			return curr_start_station
    	

g1 = (1,2,3,4,5)
c1 = (3,3,2,1,1)

g2 = (1,1,1,1,1,1,1,1,1,1)
c2 = (2,1,1,1,1,1,1,1,1,1)
s = Solution()

print s.canCompleteCircuit(g1,c1)
print s.canCompleteCircuit(g2,c2)
