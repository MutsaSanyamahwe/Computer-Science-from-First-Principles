# Stacks

 ## 1. The Problem
Imagine you're working with a collection of data where only the most recently added item should be accessed first.

Examples include:
- Undoing the last action in a text editor
- Returning from a function call
- Navigating back to the previous page
- Evaluating mathematical expressions

Using an array or linked list directly allows inserting or removing items from anywhere, making it harder to enforce this behavior.

What we need is a data structure with one simple rule:
> The last item added should always be the first item removed.

This is known as LIFO (Last In, First Out)

---
## 2. The Solution
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.

Imagine stacking books.

```
Top
 |
book 3
  |
book 2
  |
book 1
```
You can only:
- Put a book on top.
- Remove the top book.

You cannot remove the middle book without first removing the books above it.

---

 ## 3. Core Operations

**Push**
- Adds an item to the top.
- Time complexity O(1).
---

**Pop**
- Removes the top item.
- Time complexity O(1).
---

**Peek**
- Returns the top item without removing it.
- Time complexity O(1).
---

**Is Empty**
- Checks whether the stack contains any elements.
- Time complexity O(1).
---

 ## 4. How a Stack Works
A stack always keeps track of one important position:
```
Top
```
Every push moves the top upward.

Every pop moves the top downward.

```
Push A

A

Push B

B
A

Push C

C
B
A

Pop

B
A

Pop

A
```

Notice the most recently added item always leaves first.

---
## 5. Implementing a Stack
A stack is an Abstract Data Type(ADT).

It is not a specific way of storing data.

It can be implemented using:

**Arrays**
```
Index

0   1   2
A   B   C
        ↑
       Top
```

Advantages
- Excellent cache performance
- Simple implementation
- O(1) push and pop(amortized for dynamic arrays)

Disadvantages
- Fixed-size arrays can become full.
- Dynamic arrays occasionally need resizing.

 ---

 **Linked Lists**

```
Top
 ↓

C → B → A
```

Advatanges
- Grows dynamically
- No resizing required

Disadvantages
- Extra memory for pointers
- Poor cache locality.

---

 ## 6. Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |
| Search    | O(n)       |

---

## Advantages
- Very simple structure
- Fast insertion and removal
- Ideal for "undo" behavior.
- Easy to implement.
- Predictable performance.

---

## Disadvatages
- Cannot access arbitrary elements efficiently.
- Searching requires traversing the stack.
- Only the top element is directly accessible.

---

## Real-World Uses
Stacks appear throughout software engineering.

> Function Call Stack
Whenever a function calls another function:

```
main()

↓

login()

↓

validate()

↓

hashPassword()
```

Each function is pushed onto the call stack.

When a function finishes, it is popped.
---
>  Undo/Redo
Every user action is pushed.

```
Draw Circle

↓

Move Circle

↓

Delete Circle
```

Undo pops the latest action first.
---

> Browser History
The back button behaves like a stack

Visit:

```
Google

↓

YouTube

↓

GitHub
```

Press Back:

```
GitHub removed

↓

YouTube

```

---

> Expression Evaluation
Programming languages use stacks to evaluate expressions.

Example:
```
(3 + 5) × 2
```
Stacks help keep track of operators and operands

---

## Why System Designers Care
Stacks aren't usually deployed as standalone components in distributed systems, but they're fundamental to many algorithms and runtime systems.

Examples include:
- Function call management in programming language runtimes.
- Depth-First Search (DFS) in graph traversal.
- Parsing JSON, XML, and programming languages.
- Expression evaluation in interpreters and compilers.
- Backtracking algorithms.
- Undo/Redo functionality in applications

Understanding stacks helps explain how many systems manage nested operations and recursive workflows efficiently.

---

## Key Takeaways
- A stack follows the Last In, First Out(LIFO) principle.
- Only the top element can be accessed directly.
- Push, pop, and peek are O(1).
- Stacks can be implemented using arrays or linked lists.
- They are widely used in runtimes, parsers, graph algorithms, and user-facing features like undo.
---

## Questions
1. Why is a stack considered an Abstract Data Type (ADT)?

> Because it defines behavior (LIFO and operations) rather than specifying how the data is stored internally.

2. When would you implement a stack using a linked list instead of an array?
>  When you want the stack to grow dynamically without resizing.

3. What is a stack overflow?
> It occurs when more items are pushed than the stack can hold (or, in programming, when the call stack exceeds its available memory due to deep or infinite recursion).

 4. Why can't you remove an item from the middle of a stack?
> Doing so would violate the LIFO principle.

5. Why do programming languages use a call stack for function execution?
> It naturally tracks nested function calls and returns, ensuring the most recently called function completes before returning to its caller.





