
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

sol = Solution()
nums = [3,4,1,4]
print(sol.majorityElement(nums))