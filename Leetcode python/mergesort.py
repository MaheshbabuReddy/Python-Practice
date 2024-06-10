class Solution(object):
    def plusOne(self, digits):
        num = ''
        for i in digits:  
            num += str(i)
        oneplus = int(num)+1
        return [int(ele) for ele in str(oneplus)]
sol = Solution()
digits = [4,3,2,1]
print(sol.plusOne(digits))


