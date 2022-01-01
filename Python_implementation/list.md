# List

[Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

[Runtime](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

Implementation: dynamic array

### Methods

`list.append(x)`

`list.extend(iterable)`
- equivelent to `a[len(a):] = iterable`

`list.insert(i,x)`
- insert and item in a given position. `a.insert(len(a),x)` is equiv to `a.append(x)`; O(n)

`list.remove(x)`
- Remove the first item from the list whose value is equal to x. Raises a `ValueError` if there is no such item

`list.pop([i])`
- remove the item at the given position. If no param sepcified, remove the last one
- Square bracket indicate that the input is optional (notation for Python library doc)

`list.clear()`
- clear all items from the list, equiv to `del a[:]`

`list.index(x[,start[,end]])`
- Return zero-based index in the list of the first item whose value is equal x. ValueError if not found

`list.count(x)`
- Return the number of times x appears in the list

`list.sort(*,key=None, reverse=False)`
- Sort the items of the list in place

`list.reverse()`

`list.copy()`

### Use Lists as Stacks
- stack add: list.append()
- stack pop: list.pop()

### Use Lists as Queues
```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### List Comprehensions

1. List of square from 0 to 9

`squares = list(map(lambda x: x**2, range(10)))`

`squares = [x**2 for x in range(10)]`

2. List of tuples
```
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

3. Transpose of matrix

Given
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

Transpose
```
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
or
```
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```