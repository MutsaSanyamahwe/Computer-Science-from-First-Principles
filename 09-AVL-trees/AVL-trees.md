# AVL Trees

## 1. The Problem

A Binary Search Tree (BST) provides fast searching, insertion, and deletion as long as it remains balanced.

However, inserting values in sorted order can cause the tree to become skewed.

```tree
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

Instead of behaving like a tree, it behaves like a linked list.

Operations degrade from:

```text
O(log n)
```

to

```text
O(n)
```

We need a tree that automatically keeps itself balanced.

---

## 2. The Solution

An AVL Tree is a self-balancing Binary Search Tree.

It follows all the rules of a BST while ensuring the tree remains balanced after every insertion and deletion.

An AVL tree maintains the following property:
> For every node, the heights of the left and right subtrees differ by at most one.

---

## 3. Balance Factor

The Balance Factor (BF) measures whether a node is balanced.

```text
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
```

Possible values:

| Balance Factor  | Meaning                  |
| --------------- | ------------------------ |
| -1              | Balanced                 |
| 0               | Balanced                 |
| +1              | Balanced                 |
| Less than -1    | Right-heavy (Unbalanced) |
| Greater than +1 | Left-heavy (Unbalanced)  |

Example:

```text
      30
     /  \
   20    40
```

Balance Factor:

```text
30 = 0
20 = 0
40 = 0

Perfectly balanced.
```

---

## 4. How It Works
Whenever a node becomes unbalanced after an insertion or deletion, the tree performs rotations to restore balance.

The values remain in sorted order.

Only the structure changes.

---

## 5. Rotations

**Left Rotations (Right-Right Case)**

Before

```
10
  \
   20
     \
      30
```

After

```
    20
   /  \
 10   30
```

---

**Right Rotation (Left-Left Case)**

Before

```text
      30
     /
   20
  /
10
```

After

```text
    20
   /  \
 10   30
```

---

**Left-Right Rotation (LR)**

Before 

```text
      30
     /
   10
     \
      20
```

After

```text
      20
     /  \
   10   30
```

---

**Right-left Rotation (RL)**

```text
10
  \
   30
  /
20
```

After

```text
     20
    /  \
  10   30
```

---

## 6. Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Search    | O(log n)   |
| Insert    | O(log n)   |
| Delete    | O(log n)   |
| Traversal | O(n)       |

Unlike a regular BST, AVL trees guarantee these time complexities because they remain balanced.

---

## 7. Advantages

- Guaranteed O(log n) search.
- Guaranteed O(log n) insertion.
- Guaranteed O(log n) deletion.
- Automatically maintains balance.
- Excellent search performance.

---

## 8. Disadvantages

- More complex implementation.
- Rotations add overhead during insertions and deletions.
- Slightly slower updates compared to an unbalanced BST.

---

## 9. Real-World Uses

AVL Trees are useful in applications that perform many searches and require consistently fast lookups.

Examples include:
- In-memory databases.
- Search-intensive applications.
- Routing tables
- Memory management systems.
- Ordered collections.

---

## 10. Why System Designers Care

AVL Trees demonstrate an important idea:

> Maintaining additional information (such as subtree heights) can improve performance guarantees.
>
> Although AVL trees are less common than Red-Black Trees in standard libraries, they illustrate how self-balancing trees achieve reliable performance.
>
> They also prepare you for understanding:
>
> - Red-Black Trees.
> - B-Trees
> - B+ Trees
>
> These structures power many production systems.
>
> ---
>
> ## 11. BST vs AVL Tree
>
> | Binary Search Tree                 | AVL Tree                            |
| ---------------------------------- | ----------------------------------- |
| May become unbalanced.             | Always remains balanced.            |
| O(log n) average, O(n) worst case. | O(log n) guaranteed.                |
| Simpler implementation.            | More complex implementation.        |
| No rotations.                      | Uses rotations to maintain balance. |


---

## 12. Key Takeaways

- An AVL Tree is a self-balancing Binary Search Tree.
- Every node maintains a balance factor.
- Rotations restore balance after insertions and deletions.
- Search, insertion, and deletion are guaranteed to be O(log n).
- AVL Trees trade more complex updates for consistently fast lookups.


---

# Questions

1. What problem do AVL Trees solve?

> They prevent Binary Search Trees from becoming unbalanced.


2. What does AVL stand for?

> Adelson-Velsky and Landis, the two computer scientists who invented the tree.

3. Why do AVL Trees maintain subtree heights?

> To quickly determine whether a node has become unbalanced.

4. Why are AVL insertions more expensive than BST insertions?

> They may require updating heights and performing rotations.

5. How do rotations maintain the BST property?

> They rearrange parent-child relationships without changing the in-order sequence of the nodes.

6. Why does keeping the tree balanced improve performance?

> A balanced tree has a height proportional to log₂(n), reducing the number of comparisons needed for operations.

7. When would you choose an AVL Tree over a regular BST?

> When predictable, consistently fast search performance is more important than minimizing update overhead.












