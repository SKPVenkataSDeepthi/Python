# GOLDEN RULES FOR SOLVING CODING QUESTIONS

![Funny Meme](https://media.licdn.com/dms/image/v2/D4D22AQFt_XNanHmx4A/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1730006100563?e=2147483647&v=beta&t=Is6z_A2Fki4XztSUOkw3rEBKrpCIzwpZ0JnzbxkYLvY)

# RULE-1
If we are dealing with top/max/min/closest "k" elements among "N" elements, we will be using "heap".

# RULE-2
If the given input is sorted array or a list, we will be either using "binary search" or "two-pointers" strategy.

# RULE-3 
If we need to try all combinations or permutations of input we can either use "backtracking" or "bredth first search".

# RULE-4 
Most of the questions related to trees and graphs can be solved either through "breadth first search" or "Depth first search". 

# RULE-5
Every recurssive solution can be turned into iterative solution by using a "stack". 

# RULE-6 
For problem involving arrays, if there exists a solution in O(N^2) time and O(1) space there must exist 2 other solutions 
1. Using "hashmap" or "set" for O(N) time and O(N) space
2. Using sorting for O(NLogN) time and O(1) space

# RULE-7
If a problem is asking for optimization(min, max) we will be using "dynamic programming"

# RULE-8
If we need to find a common substring among a set of strings, we will be using a "hash map" or "tree". 

# RULE-9
If we need to search/manipulate a bunch of strings, "trees" will be the best data structure.

# RULE-10
If problem is related to linked lists and we can't use extra space then we use "fast and slow pointers" approach. 

# RULE-11
If we need to check whether an array contains duplicate elements within a given range, we use a "Sliding Window and Hash Set".

# RULE-12
If a problem involves scheduling tasks or prioritizing tasks based on some order, Heap (Priority Queue) or Greedy algorithms work best.

# RULE-13
If a problem requires finding the shortest path in a weighted graph, Dijkstra’s Algorithm (if all edges are non-negative) or Bellman-Ford Algorithm (if there are negative weights) is the way to go.

# RULE-14
If we are asked to find the median of a stream of numbers, use a two-heap approach (max-heap for the left half and min-heap for the right half).

# RULE-15
If a problem involves finding the "smallest/largest" missing positive number in an array, cyclic sort (or bucket sort) is a useful approach.
