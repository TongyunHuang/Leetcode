/**
This is a copy from the problem discussion
 */
public int shipWithinDays(int[] weights, int D) {
  int left = 0, right = 0;
  // figure out the searching range, each ship should be able to hold:
  // at Least the most heavy item alone
  // at most sum of all items
  for (int w: weights) {
    left = Math.max(left, w); // max of all the weights
    right += w; // sum of weights
  }
  // try capacity of ship on this range, search for the most appropriate value
  while (left < right) {
    int mid = (left + right) / 2, need = 1, cur = 0;
    for (int w: weights) {
      if (cur + w > mid) {
        need += 1;
        cur = 0;
      }
      cur += w;
    }
    if (need > D) left = mid + 1;
    else right = mid;
  }
  return left;
}