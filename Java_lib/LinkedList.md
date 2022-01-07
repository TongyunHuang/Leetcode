## LinkedList

[Documentation](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html)

Doubly-linked list implementation. Indexing takes O(n)

### Implemented interface: Queue
```
import java.util.*;

class GfG{
  public static void main(String args[]) {
    // Creating empty linkedlist
    Queue<Integer> ll = new LinkedList<Integer>();

    // adding items to the ll using add()
    ll.add(10);
    ll.add(20);
    ll.add(15);

    // print the top element
    System.out.println(ll.peak()); // print: 10

    // print the top element and remove it from the linkedList container
    System.out.println(ll.poll()); // print: 10

    // print the top element again
    System.out.println(ll.peak()); // print: 20
  }
}
```