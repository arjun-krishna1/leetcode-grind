# [14 Coding Interview Question Patterns](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
- Source: https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed
1. Sliding Window
- perform an operation on a specific window size
- on an array or linked list
- e.g. find the largest increasing subarray, find the location of weeds in the garden
- signs:
  - input is a linear data structure
    - linked list, array or string
  - you're asked to find the longest/shortest substring, subarray or a desired value
- common problems:
  - Maximum sum subarray of size 'K'
  - Longest substring with 'K' distinct characters
  - String anagrams
2. Two pointers or iterators
- two pointers iterate through a data structure in tandem
- until one or both hit a certain condition
- searching for pairs in a sorted array or linked list
- usually the same thing can be done with 1 pointer but it is much more inefficient
- signs:
  - sorted arrays or linked lists
  - find a set of elements that fulfill certain constraints
  - set of elements in the array is a pair, tripler or subarray
- e.g.
  - squaring a sorted array
  - triplets that sum to zero
  - comparing strings that contain backspaces
3. Fast and Slow pointers
- pointer algorithm
- uses two pointers to move through an array, sequence or linked list
- they move at different speeds
- useful for cyclic linked lists or arrays
- in a cyclic linked list, the pointers are bound to meet
- use over two pointers when you may need to move back in a singly linked list
  - e.g. is a linked list a palindrome? find node who's next elements sum to 0
- e.g.
  - linked list cycle
  - palindrome linked list
  - cycle in a circular array
4. Merge Intervals
- overlapping intervals
- 6 possible states of two intervals
  -  don't overlab, b ends after a
  -  overlap, b ends after a
  -  overlap, a completely overlaps b
  -  overlap, a ends after b
  -  b completely overlaps a
  -  don't overlap, a ends after b
-  signs:
  -  produce a list with only mutually exclusive intervals
  -  hear 'overlapping intervals', 'merge intervals' or 'intervals'
-  e.g.
  -  intervals intersection
  -  maximum cpu load

TODO summarize 5. Cyclic sort and after
