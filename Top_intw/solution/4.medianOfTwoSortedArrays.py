class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        """
        Sol
        """
        m,n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin+ imax)//2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i+1
            elif i > 0 and A[i-1] > B[j]:
                imax = i-1
            else:
                if i==0: max_left = B[j-1]
                elif j==0: max_left = A[i-1]
                else: max_left = max(A[i-1],B[j-1] )
                    
                if (m+n) % 2 ==1:
                    return max_left
                
                if i==m: min_right = B[j]
                elif j==n: min_right = A[i]
                else: min_right = min(A[i], B[j])
                    
                return (max_left+min_right)/2.0
        
        
        """
        Searching for the final state where:
        (1) A[i-1] < B[j] && B[j-1] < A[i]
        (2) - if m+n odd, then i+j=m+n-(i+j)-1 -> md=min(A[i], B[j])
            - if m+n even, then i+j=m+n-(i+j) -> md=(max(A[i-1],B[j-1]) + min(A[i], B[j]))(1/2)
        1. randoomly choose i,j s.t. satisfy (2)
        2. 3 cases to consider:
            (a) A[i-1]<B[j] && B[j-1]<A[i] satisfy (1) -> md find
            (b) A[i-1]<B[j] && B[j-1]>A[i], inc i, dec j
            (c) A[i-1]>B[j] && B[j-1]<A[i], inc j, dec i
        
        # initialize variables
        median = 0
        m, n = len(A), len(B)
        
        i, j = len(A) // 2, 0
        odd = False
        if (m+n) %2 == 0:
            j = ((m+n) -2*i)//2
        else:
            j = ( (m+n) - 2*i - 1 )//2
            odd = True
        
        # Start Binary Search
        while i<=m and j <= n and min(i,j)>= 0:
            print('i', i,'j',j)
            if i < m and j > 0 and B[min(0,j-1)]>A[i]:
                # print('there')
                i += 1
                j -= 1
            elif j < n and i > 0 and A[min(0,i-1)]>B[j]:
                # print('where')
                i -= 1
                j += 1
            else:
                # A[min(0,i-1)]<B[j] and B[min(0,j-1)]<A[i]
                # print('here')
                max_left, min_right = 0,0
                if i == m: min_right = B[j]
                elif j == n: min_right = A[i]
                else: min_right = min(A[i], B[j]) 
                if not odd:
                    if i==0: max_left = B[j-1]
                    elif j==0: max_left = A[i-1]
                    else: max_left = max(A[i-1],B[j-1])
                
                
                median = min_right if odd else ( max_left + min_right ) / 2
                break
        return median
    """
        