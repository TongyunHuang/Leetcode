
[TopCoder Binary search](https://www.topcoder.com/thrive/articles/Binary%20Search)
## Binary Search: The main theorem

Take away: If you were to ask the question for each element in the search space (in order), you would get a series of no answers for a predicate followed by a series of yes answers for the predicate.

### Find the predicate

When we think a problem can be solved by binary search, we aim to design the predicate so that it satisfies the condition in the main theorem

There are many problems cant be modeled as searching for a particular value, but it's possible to define and evaluate a predicate such as "Is there an assignment which costs x or less?", when we're looking for some sort of assignment with the lowest cost.

For example, the usual traveling salesman problem (TSP) looks for the cheapest round-trip which visits every city exactly onece. Here, the target value is not defined as such, but we can define a predicate "Is there a round-trip which costs x or less?" and then apply binary search to find the smallest x which satisfies the predicate. 

This is called reducing the original problem to a decision (yes/no) problem. Note that there is no way of efficiently evaluating thie particular predicate for TSP problem.
