class Solution(object):
    def findDuplicates(self, nums):
        dir = {}
        duplicates = []
        for ele in nums:
            if ele in dir:
                if ele not in duplicates:
                    duplicates.append(ele)
            else:
                dir[ele] = 1
        return duplicates

sol = Solution()
nums = [1, 3, 1, 6, 3]
print(sol.findDuplicates(nums))  