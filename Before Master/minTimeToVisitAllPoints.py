# 12/30
def minTimeToVisitAllPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    length = 0
    [prevX,prevY] = points[0]
    for [px,py] in points[1:]:
        length += max(abs(prevX - px), abs(prevY - py))
        prevX = px
        prevY = py
    return length

# main
test = minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
assert(7==test)
print(test)