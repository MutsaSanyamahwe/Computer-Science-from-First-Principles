# Linked Lists

> ## 1. The Problem
Imagine you have a list of data stored in an array.

Arrays are great because you can instantly access any element using its index.

```
Index:  0   1   2   3
Value: [A] [B] [C] [D]
```

But what happens if you want to insert a new value at the beginning?
```
Insert X

[X] [A] [B] [C] [D]
```
Every existing element has to move one position to the right.

For an array with millions of elements, this becomes expensive.

The same problem happens when deleting elements from the middle.

Arrays are efficient for random access but inefficient for frequent insertions and deletions.

---
> ## 2. The Solution
A linked list stores data differently.

Instead of storing everything next to each other in memory, every element is stored inside a node.

Each node contains:
- The actual value
- A pointer (or reference) to the next node.

Instead of relying on physical memory positions, the nodes are connected through pointers.

```
[A] → [B] → [C] → [D] → NULL
```
Since nodes don't have to be adjacent in memory, inserting or removing elements usually only requires changing a few pointers.

---
> ## 3. How It Works
A node looks like this:

```
+-----------+
| Data = A  |
| Next = •--+---->
+-----------+
```
The first node is called the Head.

```
Head
 ↓
[A] → [B] → [C] → NULL
```
To visit every node:
1. Start at the head.
2. Read the current node.
3. Follow the pointer to the next node.
4. Stop when the pointer is NULL.

Unlike arrays, you cannot jump directly to the third element.

You must walk through every previous node.

---
> ## 4. Advantages

**Fast Insertions**
Insert at the front:

Before:
```
Head
 ↓
[A] → [B] → [C]
```
After
```
Head
 ↓
[X] → [A] → [B] → [C]
```

Only one pointer changes.
---
**Fast Deletions**
Suppose we remove B.

Before
```
[A] → [B] → [C]
```
Simply make A point directly to C. No elements need to move.

---
**Dynamic Size**
Unlike arrays, linked lists don't require allocating a fixed amount of memory.

Nodes are created only when needed.
---
> ## 5. Disadvantages

**Slow Random Access**
Want the 1000th node?

Arrays:
```
Array[999]
```
Linked Lists:
```
Head
 ↓
1 → 2 → 3 → 4 → ...
```
You must visit every node before reaching the target.
---

**Extra Memory**
Each node stores:
- Data
- Pointer
Arrays only store the data. So linked lists use more memory.
---

**Poor Cache Performance**
Array memory:
```
[A][B][C][D][E]
```
Everything is together next to each other.

Linked list memory:
```
[A]

        [D]

[B]

             [E]

      [C]
``` 
Nodes may be scattered throughout memory, causing more cache misses.
---

> ## 6. Time Complexity
| Operation           | Array          | Linked List                      |
| ------------------- | -------------- | -------------------------------- |
| Access by index     | O(1)           | O(n)                             |
| Search              | O(n)           | O(n)                             |
| Insert at beginning | O(n)           | O(1)                             |
| Insert at end*      | O(1) amortized | O(n) (or O(1) with tail pointer) |
| Delete at beginning | O(n)           | O(1)                             |
| Delete in middle    | O(n)           | O(n)                             |


> ## 7. Variations

### Singly linked List
Each node points to the next node.

```
A → B → C → NULL
```
---

### Doubly Linked List
Each node points to both the next and the previous nodes.

```
NULL ← A ⇄ B ⇄ C → NULL
```
This allows moving in both directions but requires extra memory.
---
### Circular Linked List
The last node points back to the first.
```
A → B → C
↑       ↓
└───────┘
```
Useful for systems that repeatedly cycle through data, such as round-robin schedulers.

---

> ## 8. Real-World Uses
Linked lists are common when frequent insertions and deletions matter more than random access.

Examples include:
- Music playlists (next, previous song)
- Browser back/forward history
- Undo/redo functionality in editors
- LRU cache implementations
- Memory allocators in operating systems
- Hash table collision handling (separate chaining)
- Graph adjacency lists
---

> ## 9. Why System Designers Care

Linked lists are rarely used directly in large-scale distributed systems, but they form the building blocks of many important data structures.

Examples include:
- Hash maps that use linked lists to resolve collisions
- LRU caches that combine a hash map with a doubly linked list for O(1) lookups and eviction
- Memory allocators that maintain free blocks as linked lists
- Graph representations using adjacency lists

Understanding linked lists helps explain how these higher-level systems achieve their performance characteristics.

> ## 10. Key Takeaways
- Arrays store elements next to each other in memory.
- Linked lists connect nodes using pointers.
- Insertions and deletions are efficient because only pointers change.
- Random access is slow because nodes must be traversed sequentially.
- Every node stores both data and a pointer, increasing memory usage.
- Doubly linked lists allow traversal in both directions.
- Linked lists are foundational for many advanced data structures used in system design.


