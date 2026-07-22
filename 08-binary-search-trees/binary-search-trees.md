# Binary Search Trees (BSTs)

## 1. The Problem

A binary tree organizes data hierarchically, but it doesn't impose any ordering rules.

For example:

```text
        20
       /  \
     50    10
    / \    / \
   5  30 40  60
```

If we want to find `40`, there's no way to know which direction to go.

We may need to search every node.

Searching in a general binary tree is therefore O(n).

We need a way to organize the tree so that searching becomes much faster.

---

## 2. The Solution

A **Binary Search Tree (BST)** is a binary tree that follows one simple rule:
- Every value in the left subtree is less than the current node.
- Every value in the right subtree is greater than the current node.

Example:

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40 60   80
```

This ordering allows us to eliminate half of the remaining tree at each step, similar to binary search on a sorted array.

---

## 3. How It Works

Suppose we want to find `60`.

Start at the root.

```text
50
```

Since `60 > 50 `, move right.

```text
70
```

Since `60 < 70`, move left.

```text
60 found
```

The value is found without visiting every node.

---

## 4. BST Operations

**Search**
Compare the target with the current node.

- smaller - go left
- larger - go right
- equal - found

- Average Time Complexity:

```text
O(log n)
```

---

**Insert**

Insertions follow the same rule as searching.

Insert `65`.

```text
Before

        50
       /  \
     30    70
          /
        60

```


```text
After

        50
       /  \
     30    70
          /
        60
          \
          65
```

---

**Delete**

Deletion has three cases.

*Case 1: Leaf Node*

Simply remove it.

```text
50
 \
 70
```

Delete `70`  

```text
50
```

*Case 2: One Child*

Replace the node with its child.

```text
50
 \
 70
 /
60
```

Delete `70 `

```text
50
 \
 60
```

*Case 3: Two Children*

Replace the node with its inorder successor (smallest value in the right subtree) or inorder predecessor (largest value in the left subtree).

| Operation | Average  | Worst |
| --------- | -------- | ----- |
| Search    | O(log n) | O(n)  |
| Insert    | O(log n) | O(n)  |
| Delete    | O(log n) | O(n)  |
| Traversal | O(n)     | O(n)  |

The worst case occurs when the tree becomes unbalanced.

---

## 6. Balanced vs Unbalanced Trees

Balanced BST:

```text
        50
      /    \
    30      70
   / \      / \
 20 40    60 80
```

Height is approximately log₂(n).

Operations remain fast.

---

Unbalanced BST:

Insert values in sorted order.

```text
10
 \
 20
   \
   30
     \
     40
       \
       50
```
The tree behaves like a linked list.

Operations degrade to:

```text
O(n)
```

---

## 7. Advantages
- Fast searching.
- Fast insertions
- Maintains sorted order.
- Supports sorted order.
- Supports efficient range queries.
- Foundation for many advanced trees.


---

## 8. Disadvantages
- Performance depends on tree balance.
- Can degrade into a linked list.
- More complex than arrays or linked lists.

---

## 9. Real-World Uses

Binary Search Trees are useful whenever data must remain ordered.

Examples include:
- In-memory sorted collections.
- Leaderboards and ranking systems
- Symbol tables in compilers
- Range-based queries
- Scheduling systems

Many real-world systems use self-balancing variants rather than plain BSTs.

---

## 10. Why System Designers Care

A plain BST is rarely used directly in production because it can become unbalanced.

However, it introduces the concepts behind:
- AVL trees
- Red-Black trees
- B-trees
- B+ trees

These structures power:
- Database indexes
- File systems
- Language libraries (e.g., Java's `TreeMap` and `TreeSet`)
- Operating systems

Understanding BSTs is essential before learning how modern databases perform fast searches.

## 11. Key Takeaways
- A BST is a binary tree with an ordering rule.
- Left subtree values are smaller than the parent.
- Right subtree values are larger than the parent.
- Search, insert, and delete are O(log n) on average.
- Unbalanced BSTs can degrade to O(n).
- Self-balancing trees solve this problem.

---

# Questions

1. Can duplicate values exist in a BST?

> It depends on the implementation. Some allow duplicates with specific rules, while others require keys to be unique.

2. Why can a BST degrade to O(n)?

> Because an unbalanced tree may have a height of n, forcing operations to traverse almost every node.

3. Why are AVL and Red-Black Trees preferred in production?

> They automatically maintain balance, guaranteeing O(log n) operations.



