class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        indexOfBiggest = 0
        biggest = None
        for x in range(0, len(num)):
            if (biggest is None or num[x] > biggest):
                indexOfBiggest = x
                biggest = num[x]
            if (x>0 and x<(len(num)-1)):
                if (num[x-1] < num[x] and num[x+1] < num[x]):
                    print x
                    return x
        print indexOfBiggest
        return indexOfBiggest


s = Solution();
s.findPeakElement([1,1,1,2,1]);
s.findPeakElement([1]);
s.findPeakElement([1,2]);
s.findPeakElement([-2000, -300]);
