"""
My idea
use stack to keep track of the bars  that are bounded by longer bars and thus can store water
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        lowest = height[0]
        water = 0
        stack = [(0,height[0])]
        for i in range(1, len(height)):
            if height[i] <= height[i-1]:
                stack.append((i,height[i]))
                lowest = min(lowest,height[i])
            else:
                while len(stack) >0:
                    curPop = stack.pop(-1)
                    if curPop[1] != lowest:
                        addHeight = (min(height[i],curPop[1])-lowest)
                        addWater = (i-curPop[0]-1)*addHeight
                        water += addWater
                        lowest += addHeight
                    if curPop[1] == height[i]:
                        break
                    if curPop[1] > height[i]:
                        stack.append(curPop)
                        break
                stack.append((i,height[i]))
        return water
                
"""
SOl Idea: two pointers
maintaitn 5 variables: left_ptr, right_ptr, left_max, right_max, water
while left_ptr < right_ptr
1. if height[left] < height[right]
    - if height[left] > left_max, update left_max
    - else add left_max-height[left] to water
    - increment left_ptr
2. if height[right] < height[left]
    - if height[right] > right_max, update right_max
    - else add right_max - height[right] to water
    - decrement right_ptr
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr, right_ptr, left_max, right_max = 0, len(height)-1, 0, 0
        water = 0
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] > left_max:
                    left_max = height[left_ptr]
                else:
                    water += left_max - height[left_ptr]
                left_ptr += 1
            else:
                if height[right_ptr] > right_max:
                    right_max = height[right_ptr]
                else:
                    water += right_max - height[right_ptr]
                right_ptr -= 1
        return water
                