class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
	    previous = None
	    dupeCount = 0
	    for x in xrange (len(A)-1, -1, -1):
		    if previous == A[x]:
			    A.remove(previous)
	            previous = A[x]
	    print A
	    return len(A)


s = Solution();
s.removeDuplicates([1,1,2,2,3]);

		    

