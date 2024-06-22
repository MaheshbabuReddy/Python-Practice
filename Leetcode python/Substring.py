def Subsequence(s,t):
    if len(s) > len(t):
        return False
    else:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j +=1
                if i == len(s):
                    return False
                return True
            

s = "axc"
t ="ahbgdc"
print(Subsequence(s,t))
