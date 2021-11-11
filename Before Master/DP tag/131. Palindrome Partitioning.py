'''
== Approach 1: Backtracking ==
* Generate all possible substrings of a given string and expand each possibility if is a possible candidate.
* The first thing that comes to out mind is DFS.
* In DFS, we recursively expand potential candidate until the defined goal is achieved. After that, we backtrack to explore the next potential candidate

* Backtracking incrementally build tha candidates for the solution and discard the candidates (backtrack) if it doesnt satidfy the condition
* The backtracking algo consists of the following steps:
- choose: choose the po
'''

'''
Algo:
In the backtracking algorithm, we recursively traverse over the string in DFS fashion. For each resursivel call, the beginning index of the string is given as start
1. Iteratively generate all possible substrings beginning at start index. The end index increments from start till the end of the string
2. For each of the subtring generated, check if it is a palindrome
3. If the substring is a palindrome, the substring is a potential candidate. Add substring to the currentList and perform a DFS on the remaining substring. If current substring ends at index end, end + 1 becomes the start index for the next recursive call.

'''
'''@parameter s:str'''
'''Helper function that check if the substring from start to end is a palin'''


def isPalindrome(s, start, end):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
        if i == n-1-i or i+1 == n-1-i:
            return True
    return True


''' Main Function'''


def allPalin(s, start, end):
    allPair = []
    # loop over all possible start index
    for i in range(start, end):
        prePalin = allPalin(s, 0, i-1)
        for j in range(i+1, end):
            if isPalindrome(s, i, j):
                postPalin = allPalin(s, j+1, len(s))
                for pre in prePalin:
                    for post in postPalin:
                        allPair.append(pre.append(s.substr(i, j)) + post)
    return allPair


def dfs(start, result, currList, s):
    res = [[]]
    if start >= len(s):
        currList_copy = currList
        res.append(currList_copy)
    for end in range(start, len(s)):
        if isPalindrome(s, start, end):
            # add current substring in the currentList
            currList.add(s[start:end+1])
            dfs(end+1, result, currList, s)
            # backtrack and remove the current substring from currList
            currList.pop(len(currList)-1)
