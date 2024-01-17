class Solution(object):
    def romanToInt(self, s):
        #small before Large = Substraction shoud be perform IV=4 because (I=1,V=5  1-5=4)
        #Large befor Small= Addition shoud be perform XI=11 baecause (X=10, I=1 10+1=11)
        self.s = s
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_val[s[i]] < roman_val[s[i+1]]:
                val -= roman_val[s[i]]
            else:
                val += roman_val[s[i]]
        return val

s = "MCMXCIV"
sol = Solution()
result = sol.romanToInt(s)
print(result)

      

            
            