class Solution:
    def fib(self, n: int) -> int:
        trans=[0,1]
        ##1定义初始状态
        for i in range(2,n+1):
            ## 2转移方程
            trans.append(trans[i-2]+trans[i-1])
        return trans[n]
a=Solution()
print(a.fib(6))