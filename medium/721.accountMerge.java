/**Copy of solution from leetcode */
class DSU {
  int representative [];
  int size [];

  /** Constructor */
  DSU(int sz) {
    representative = new int[sz];
    size = new int[sz];
    for (int i = 0; i < sz; ++i) {
      // Initially each group is its own representative
      representative[i] = i;
      size[i] = 1;
    }
  }

  /* Find representative  @param x */
  public int findRepresentative(int x) {
    if (x == representative[x]) {
      return x;
    }
    return representative[x] = findRepresentative(representative[x]);
  }

  /* unite the group that contains "a" with the group that contains "b" */
  public void unionBySize(int a, int b) {
    int repreA = findRepresentative(a);
    int repreB = findRepresentative(b);

    if (repreA == repreB) {
      return;
    }
    // group to the larger group
    if (size[repreA] >= size[repreB]) {
      size[repreA] += size[repreB];
      representative[repreB] = repreA;
    } else {
      size[repreB] += size[repreA];
      representative[repreA] = repreB;
    }
  } 
}// end of DSU class

class Solution {
  /* Function get called */
  public List<List<String>> accountsMerge(List<List<String>> accountList) {
    int accountListSize = accountList.size();
    DSU dsu = new DSU(accountListSize);
    
    Map<String, Integer> emailGroup = new HashMap<>();
    // traverse through emails and update dsu accordingly
    for (int i = 0; i < accountListSize; i++) {
      int accountSize = accountList.get(i).size();

      for (int j = 1; i < accountSize; j++) {
        String email = accountList.get(i).get(j);
        String accountName = accountList.get(i).get(0);
        if (!emailGroup.containsKey(email)) {
          emailGroup.put(email,i);
        } else {
          dsu.unionBySize(i, emailGroup.get(email));
        }
      }
    }

    // Store emails corresponding to the component's representative
    Map<Integer, List<String>> components = new HashMap<Integer, List<String>>();
    for (String email : emailGroup.keySet()) {
      int group = emailGroup.get(email);
      int groupRep = dsu.findRepresentative(group);

      if (!components.containsKey(groupRep)) {
        components.put(groupRep, new ArrayList<String>());
      }
      components.get(groupRep).add(email);
    }

    // Sort the components and add the account name
    List<List<String>> mergedAccounts = new ArrayList<>();
    for (int group:components.keySet()) {
      List<String> component = components.get(group);
      Collections.sort(component);
      component.add(0, accountList.get(group).get(0));
      mergedAccounts.add(component);
    }
    return mergedAccounts;
  }
}
