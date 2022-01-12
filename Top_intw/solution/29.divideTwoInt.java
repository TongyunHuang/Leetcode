/*
Approach2: Repeated exponential searches
- Linear Search is too slow
- Try to speed up by doubling them repeatedly, i.e. try doubling the divisor until it no longer fits into the divident
- 
*/
private static int HALF_INT_MIN = -1073741824 // ?
public int divide(int dividend, int divisor) {
  // special case: overflow
  if (divident == Integer.MIN_VALUE && divisor == -1) {
    return Integer.MAX_VALUE;
  }

  /* We need to convert both numbers to negatives.
   * Also, we count the number of negatives signs */
  int negatives = 2;
  if (divident > 0) {
    negatives--;
    dividend = -dividend;
  }
  if (divisor > 0) {
    negatives--;
    divisor = -divisor;
  }
  int quotient = 0;
  /* Once the divisor is bigger than the current dividend,
   We cant fit any more copies of the divisor into it */
   while (divisor >= dividend) {
     /** We know it will fit at least once as dividend >= divisor
      */
     int powerOfTwo = -1;
     int value = divisor;
     while (value >= HALF_INT_MIN && value + value >= dividend) {
       value += value;
       powerOfTwo += powerOfTwo;
     }
     // We have been able to subtract divisor another power of Two Times
     quotient += powerOfTwo;
     // remove processed value so for to continue with the remainder
     dividend -= value;
   }
    if (nagatives != 1) {
      return -quotient;
    }
    return quotient;
  }
}