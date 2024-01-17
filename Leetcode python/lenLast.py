class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        self.s=s
        x= s.strip()
        for i in x:
            if i == " ":
                count = 0
            else:
                count += 1
        return count
sol=Solution()
s="   fly me   to   the moon  "
print(sol.lengthOfLastWord(s)) 