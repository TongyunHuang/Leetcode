"""
Idea
1. Define a data structure (with class) to perform union find
    - perform 'findRepresentative' and 'union'
2. Traverse all emails.Use map <str:email, int:accIdx>
    - if email already in map => acc existed => union rep of two account
    - otherwise, plug in value to map
3. Wrap up
    (1) construct dic, <int:representative, arr: emails of the rep>
    (2) sort all email list and insert account name at front
"""
class unionSet:
    def __init__(self,size):
        self.representative = [i for i in range(size)]
        # self.size = [0 for i in range(size)]
    def getRep(self):
        return self.representative
    def find_representative(self, idx):
        res = -1
        while True:
            res = self.representative[idx]
            if res == idx: break
            idx = res
        return res
    
    def union(self,a,b):
        repA = self.find_representative(a)
        repB = self.find_representative(b)
        if repA < repB:
            self.representative[repB] = repA
        if repB < repA:
            self.representative[repA] = repB
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accLen = len(accounts)
        # initialize unionSet object and dict <str:email, num:accIdx>
        ds = unionSet(accLen)
        dic = {}
        # traverse email and setup corres acc idx
        for i in range(accLen):
            infoLen = len(accounts[i])
            info = accounts[i]
            for j in range(1, infoLen):
                email = info[j]
                emailAcc = dic.get(email, None)
                if emailAcc is None:
                    dic[email] = i
                else:
                    ds.union(i,emailAcc)
        # Wrap up
        resAcc = {}
        # 1. store emails corresponding to representative
        for email in dic.keys():
            accIdx = dic[email]
            rep = ds.find_representative(accIdx)
            if resAcc.get(rep, None) is None:
                resAcc[rep] = [email]
            else:
                resAcc[rep].append(email)
        
        res = []
        # 2. sort lists in resAcc and add account name
        for rep in resAcc.keys():
            email_list = resAcc[rep]
            email_list = sorted(email_list)
            email_list.insert(0, accounts[rep][0])
            res.append(email_list)
        return res
                    
                