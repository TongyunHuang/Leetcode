class Solution:
    """
    Idea:
    - maintain a list of index according to frequenci of the index
    - maintain am index in round
    """
    def __init__(self, w: List[int]):
        self.k = 0
        self.w = w
        self.randomList = []
        summ = 0
        for i in range(len(w)):
            summ += w[i]
            self.randomList.append(summ)
        self.summ = summ

    def pickIndex(self) -> int:
        r = self.summ * random.random()
        start, end = 0, len(self.w)
        while start < end:
            mid = (start + end) // 2
            # checked sol
            if r > self.randomList[mid]:
                start = mid + 1
            else:
                end = mid
        return start
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()