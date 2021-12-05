def binomCoeff(n: int, k: int) -> int:
    k = min(k, n-k)

    coeff = 1
    for i in range(k):
        coeff *= (n - i)
        coeff //= (i + 1)
    return coeff


class Solution:
    def numTrees(self, n: int) -> int:
        answer = binomCoeff(2*n, n)
        answer //= (n + 1)
        
        return answer
