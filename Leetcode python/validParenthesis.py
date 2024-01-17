class Solution(object):
    def isPalindrome(self, s):
        self.s = s

        def isAlphanumeric(char):
            return char.isalnum()
        new =list(filter(isAlphanumeric, s.lower()))
        left, right = 0, len(new) - 1
        while left < right:
            if new[left] == new[right]:
                return True
            left += 1
            right -= 1

        return False
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
