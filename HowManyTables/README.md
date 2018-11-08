# HowManyTables Problem
## By: Oscar Vanderhorst

My following solution is an alternative approach to UnionFind utilizing linked list.

In my solution, I use an array filled with Table objects that in them have a list of numbers (people & index) to follow the unions.

Given these, my solution will on worst case utilize:

### O(2n) = O(n) space. Where n = amount of people.
### O(n*m) time. Where m = amount of statements.