class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
	    elements = {}
	    for n in num:
		    if n in elements.keys():
			    elements[n] = elements[n] + 1
			    
		    else:
			    elements[n] = 1;

	            if elements[n] > len(num)/2:
			    print n
			    return n

s = Solution();
s.majorityElement([1]);
s.majorityElement([1,2,3,2,2,2,4]);
s.majorityElement([0,5,10,0,0,1,0]);
	
		
	
		



