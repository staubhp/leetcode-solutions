class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
            for x in range (0,k):
                    nums.insert(0,nums.pop(len(nums)-1))
            print(nums)
            

s = Solution()
s.rotate([1,2,3,4,5,6,7],3)

