# Binary Trees

## 1. The Problem

So far, we've looked at data structures that store data in a linear fashion.

```
A → B → C → D → E
```

This works well for many use cases, but searching through large amounts of ordered data can become inefficient.

For example, if we store one million sorted numbers in a linked list, finding a value may require traversing many nodes.

We need a way to recognize data that allows us to search, insert, and delete more efficiently while maintaining relationships between elements.

---

## 2. The Solution

A binary tree is a hierarchical data structure where each node can have at most two children:
- A left child
- A right child

Instead of storing data in a line, a binary tree branches out.

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

The top node is called the root, and every child node can itself become the root of another subtree.

---

## 3. Key Concepts

### Node

A node stores:
- Data
- A reference to the left child
- A reference to the right child

```
+----------------+
| Data = A       |
| Left  = •      |
| Right = •      |
+----------------+
```

### Root

The first node of the tree.

```
    A
```

### Parent and Child

```
    A
   / \
  B   C
```

- A is the parent of B and C.
- B and C are children of A.

### Leaf

A node with no children.

```
    A
   / \
  B   C
     / \
    D   E
```

Leaves:
- B
- D
- E

### Height

The height of a tree is the number of edges on the longest path from the root to the leaf.

---

## 4. How It Works

Unlike linked lists, a node can point to two other nodes.

```
        50
       /  \
     25    75
    / \    / \
  10 40 60 90
```

To find a value, algorithms traverse the tree following parent-child relationships.

Different traversal strategies visit nodes in different orders.

---

## 5. Tree Traversals

### Preorder

Vist:
```
Root → Left → Right
```

Example:

```
        A
       / \
      B   C
     / \
    D   E
```

Result:

```
A B D E C
```

--- 

### Inorder

Visit:

```
Left → Root → Right
```
Example:

```
        A
       / \
      B   C
     / \
    D   E
```

Result:

```
D B E A C
```

---

PostOrder

Visit:

```
Left → Right → Root
```

Example:

```
        A
       / \
      B   C
     / \
    D   E
```



Result:

```
D E B C A
```

---

### Level Order

Visit one level at a time using a queue.

Example:

```
        A
       / \
      B   C
     / \
    D   E
```

Result:

```
A B C D E
```

---

## 6. Time Complexity

For a general binary tree:

| Operation | Complexity |
| --------- | ---------- |
| Search    | O(n)       |
| Insert    | O(n)       |
| Delete    | O(n)       |
| Traversal | O(n)       |

> A regular binary tree has no ordering rules, so searching may require visiting every node.


---

## 7. Advantages
- Represents hierarchical relationships naturally.
- Easy to traverse recursively.
- Forms the basis of many advanced data structures.
- Flexible and dynamic.

---

## 8. Disadvantages
- No guaranteed fast searching
- Can become unbalanced
- More memory overhead than arrays.

---

## 9. Real-World Uses
Binary trees appear in many areas of software engineering.

Examples include:

- Expression trees in compilers.
- Decision trees in machine learning.
- File system hierarchies.
- XML and HTML document parsing.
- Game AI decision making.

Many advanced tree structures are built from the same concepts.

---


## 10. Why System Designers Care

 Binary trees are rarely used directly in large-scale systems, but they provide the foundation for more advanced tree structures.

 Examples include:
 - Binary Search Trees (BSTs)
 - AVL Trees
 - Red-Black Trees
 - B-Trees
 - B+ Trees

These structures power:
- Database indexes
- File systems
- Memory management
- Programming language libraries

Understanding binary trees is essential before learning how databases and operating systems organize data efficiently.

---

## 11. Key Takeaways
- A binary tree is a hierarchical data structure.
- Each node has at most two children.
- Nodes are connected through parent-child relationships.
- Traversal algorithms visit nodes in different orders.
- Binary trees are the foundation of many advanced tree structures.

# Questions

1. Why isn't searching always fast in a binary tree?

> Because a general binary tree has no ordering rules, so you may need to visit every node.

2. Why are trees considered hierarchical rather than linear?

> Because each node can branch to multiple children instead of forming a single chain.


3. Why is recursion commonly used with trees?

> Because each subtree is itself a smaller tree, making recursive solutions natural.

4. How can an unbalanced tree affect performance?

> It can degrade operations to O(n), similar to a linked list.

