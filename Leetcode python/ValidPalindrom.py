class Solution:
    def isPalindrome(self,s):
        sen=''
        for word in s:
            if word.isalnum():
                sen += word.lower()           
        i = 0
        j = len(sen)-1
        while i < j:
            if s[i] != sen[j]:
                return False
            i+= 1
            j-= 1
        return True
solution = Solution()
s = "race a car"
print(solution.isPalindrome(s))