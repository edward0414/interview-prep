# Interview Study Guide

## Algorithms

### Tree Traversal
- **In order**
- **Post order**
- **Pre order**
- **Depth first search** (Stack: last added child go next when popped)
- **Breadth first search** (Queue: popped in order, iterate through each level)
- **Uniform cost** (PriorityQueue: similar to bfs, but pop the one with the least _cost_ using priorityQueue)
- **Heuristic**  (PriorityQueue: similar to bfs, but pop the one with the least _cost + heuristic_ value using priorityQueue)

### Stack & Queue
- could be use intelligently to:
	- implement searching algor iteratively
	- check balance of a string (push or pop)

- Stack: regular python list (append + pop)
- Queue: regular python list (insert[0] + pop)

### Object-oriented Programming
- create a class
	- method
	- private variable
	- public variable
	- static method

- when to create a class?
	- grid class instead of 2d array
	- when you can use that to validate data (helper method)

### Hashmap (constant search time)
- extremely useful and common 
- classic question: 2 Sum

### Priority Queue 


## Thinking Process
### Step 1
- Draw out the question
- Ask for clarification on anything that is not 100% clear to you
- List out the edge cases(s) if applicable
- Think of a brute-force algor
- THINK OUT LOUD!!

### Step 2
- Think about how to improve it by using Hashmap, Stack, or Queue
- Check if you are on the right track
- then, check advanced technique: sliding window, dynamic programming
- if searching, check: tree traversal, recursive method

### Additional
- point out if the space vs time trade-off
- eg. for better space complexity, use this; better time complexity, do that
- Big-O analysis

## Questions
### Reverse a linked list
### 3 Sum
### parlindrome
### Anagram
