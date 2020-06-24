def binomialCoeff(n, k):    
    res = 1

    if k > n - k:  
        k = n - k

    for i in range(k):  
        res = (res * (n - i)  ) // (i + 1)

    return res  
    
class Solution:
    def numTrees(self, n: int) -> int:
        c = binomialCoeff(2 * n, n)    
        return c // (n + 1)  
    