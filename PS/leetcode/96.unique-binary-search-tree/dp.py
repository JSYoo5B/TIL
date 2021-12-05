class Solution:
    def numTrees(self, n: int) -> int:
        # list idx means when it becomes root
        kinds = [ 0 for _ in range(n + 1) ]
        
        # for elems 0, 1. it starts with 1 kind
        kinds[0] = kinds[1] = 1
        
        for root in range(2, n+1):
            for subnode in range(1, root+1):
                kinds[root] += kinds[subnode-1] * kinds[root-subnode]
                
        return kinds[n]
