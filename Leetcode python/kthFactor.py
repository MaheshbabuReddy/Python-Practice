class Solution(object):
    def kthFactor(self, n ,k):
        self.n=n
        self.k=k
        li=[]
        for i in range(1,n+1):
            if n % i == 0:
                li.append(i)
        for ele in range(len(li)):
            if k-1 == ele :
                return li[ele]
        return -1

n=12
k=3
sol=Solution()
s=sol.kthFactor(n,k)
print(s)

