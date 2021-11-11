class Solution(object):
    def maxSubarraySumCircular(self,A):
        """
        N = len(A)
        ans = cur = None
        for x in A:
            cur = x + max(cur,0)
            ans = max(ans, cur)
        
        # ans is tha answer for 1-interval subarrays
        # Now, let's consider all 2-interval subarrays
        #  for each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])
        rightsums = [None] *N
        rightsums[-1] = A[-1]
        for i in range(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]
        
        maxright = [None] * N
        """
        def kadene(gen):
            # Maximum non-empty subarrray sum
            ans = cur = None
            for x in gen:
                cur = x+max(cur,0)
                ans = max(ans,cur)
            return ans
        
        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1,len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A),1))
        return max(ans1, ans2, ans3)
