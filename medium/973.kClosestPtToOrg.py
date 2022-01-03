class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Idea:
        use hashmap, key: dist, value: index
        dict.keys get list -> k quickselect
        add all smaller than k to result list
        """
        # hashmap store distance
        dic = {}
        dists = []
        for index in points:
            dist = pow(index[0],2) + pow(index[1],2)
            dists.append(dist)
            if dic.get(dist, None) is not None:
                dic[dist].append(index)
            else:
                dic[dist] = [index]
        
        # quickselect k
        # dists = [k for k in dic]
        kNum = self.quickSelect(dists, k, 0, len(dists)-1)
        # print('kNum', kNum)
        # add all smaller than k to result list
        res = []
        for k in dic:
            if k <= kNum:
                for x in dic[k]:
                    res.append(x)
        return res
    
    def quickSelect(self, dists, k, left, right):
        if left < right:
            pivot = self.partition(dists, k, left, right)
            
            if pivot == k-1:
                return dists[pivot]
            elif pivot < k-1:
                return self.quickSelect(dists, k, pivot+1, right)
            else:
                # print(left, pivot-1)
                return self.quickSelect(dists, k, left, pivot-1)
        elif left == right:
            # print('here', dists[left])
            return dists[left]
    
    def partition(self, dists, k , start, end ):
        pivot = start
        # print(dists[pivot], start, end)
        curr = start+1
        for i in range(start+1, end+1):
            if dists[i] <= dists[pivot]:
                dists[curr], dists[i] = dists[i], dists[curr]
                curr += 1
        # curr = min(end, curr)
        dists[curr-1], dists[pivot] = dists[pivot], dists[curr-1]
        
        pivot = curr-1
        # print(dists, pivot)
        return pivot
                
        