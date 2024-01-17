class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j
solution = Solution()
nums = [3,2,2,3]
val = 3
k = solution.removeElement(nums, val)
print(nums[:k])  
print(k)