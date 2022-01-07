/* ################################### Array ##################################### */

/* Declaration */
// 1. Empty
int intArray[];
intArray = new int[20];
// OR
int intArray = new int[20];

// 2. With numbers
int[] intArray = new int[]{1,2,3,4};

/* Remove */
int[] arr = {1,2,3,4,5,6};
int index = 2;
arr = ArrayUtils.remove(arr, index);

/* Add element */
// Create a new array with size n+1 and copy the array over
// Or change it to ArrayList, call add, and go back
public static Integer[] addX(int n, Integer arr[], int x) {
  int i;
  // create a new ArrayList
  List<Integer> arrlist = new ArrayList<Integer>(Arrays.asList(arr));
  // add the new element
  arrlist.add(x);
  // change back to arr
  arr = arrlist.toArray(arr);
  return arr;
}

/* Print array */
System.out.println("Initial Array: \n"
                    + Arrays.toString(arr));

/* Stack: interface of vector 
 * Stack<Integer> stack = new Stack<Integer>();
 * empty() - tests if the stack is empty
 * peek() - looks at the object at the top of this stack and returns that object as the value of this function
 * pop() - removes the object at the top of the stack and returns that object as the value of this function
 * push() - pushes an item onto the top of this stack
 * search(Object o) - returns the 1-based position where an object is on this stack
  */

/** ############################################ ArrayList ######################## */


/** ####################################### TYPES  ################### */
// int to Integer
int iInt = 10;
Integer iInteger = Integer.valueOf(iInt);
// ascii to string
String asciiStr = Character.toString(65); // "A"


/** ################################## STRING ########################################## */
// STRING BUILDER: A mutable sequence of characters
// Append
String str = new StringBuilder().append('a').append('b').toString();


