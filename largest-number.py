class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
            slist = []
            output = ''

            def comparator(a,b):
                    ab = int(str(a)+str(b))
                    ba = int(str(b)+str(a))
                    return ab if ab > ba else ba


            for y in range(9,0,-1):
                    matches = [x for x in num if str(x)[0] == str(y)]
                    matches.sort(reverse=True)
                    if not matches:
                            continue
                    if len(matches) == 1:
                            output += str(matches[0])
                            continue
                    for m in range(0,len(matches)-1,2):
                            output += str(comparator(matches[m],matches[m-1]))

            return output



s = Solution()
s.largestNumber([98,9, 91, 94])
s.largestNumber([1,121])
s.largestNumber([1])
s.largestNumber([1,1,1])
                            


                    

        
