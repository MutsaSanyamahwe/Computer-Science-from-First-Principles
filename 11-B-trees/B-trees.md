# B- Trees

## 1. The Problem

Binary Search Trees are efficient when data fits comfortably in memory.

However, large datasets are often stored on secondary storage, such as:

- SSDs
- Hard drives
- Database storage
- File systems

Accessing secondary storage is much more expensive than accessing data already in memory.

A traditional Binary Search Tree can become very tall:

```
                50
               /  \
             30    70
            / \    / \
          20  40  60  80
         /
       10
      /
     5
```

Searching through many levels requires many separate storage accesses.

We need a tree that:

- Keeps its height small
- Stores multiple keys in each node.
- Reduces the number of storage accesses.
- Remains balanced
- Still provides efficient search, insertion, and deletion.

---

## 2. The Solution

A B-Tree is a self-balancing search tree designed to store and retrieve large amounts of data efficiently.

Unlike a Binary Search Tree, where each node normally contains one key and has at most two children, a B-Tree node can contain multiple keys and multiple children.

For example:

```
              [30 | 60]
             /    |    \
            /     |     \
     [10 | 20] [40 | 50] [70 | 80 | 90]
```

The keys inside each node are sorted.

The children represent ranges of values.

For example:

```
              [30 | 60]
             /    |    \
            /     |     \
        < 30   30-60     > 60
```

This allows a B-Tree to store much more information at each level.

The result is a much shorter tree.

---

## 3. Why Multiple Keys Per Node?

This is the key idea behind B-Trees.

Consider a binary tree:

```
          50
        /    \
      30      70
     /  \    /  \
   20   40  60   80
```

Each node contains one key.

Now consider a B-Tree:

```
              [30 | 50 | 70]
             /    |    |    \
           [10] [40]  [60]  [80]
```

One node can now represent several values and several ranges.

This dramatically reduces the number of levels required.

### Why does it matter?

Suppose we have millions of records.

A binary tree might require many levels.

```
Level 1
   ↓
Level 2
   ↓
Level 3
   ↓
Level 4
   ↓
Level 5
   ↓
...
```

A B-Tree can store many keys per node:

```
Level 1       [20 | 40 | 60 | 80]
             /    |    |    |    \
Level 2    [ ... ][ ... ][ ... ][ ... ]

Level 3    [ ... ][ ... ][ ... ][ ... ]
```

The tree therefore becomes wide instead of tall.

That is extremely useful when each level may require disk/SSD access.

---

## 4. B-Tree Properties

A B-Tree follows several important rules.

### Rule 1 - Keys inside a node are sorted

For example:


```
[20 | 40 | 70]
```

The keys must be ordered.

---

### Rule 2 - A node can contain multiple keys

Unlike a Binary Search Tree:

```
[50]
```

A B-Tree node might contain:

```
[20 | 40 | 50 | 70 | 90]
```

The exact number depends on the tree's order.

--- 

### Rule 3 - A node with `k` keys can have up to `k+1` children

For example:

```
          [30 | 60]
         /    |    \
        /     |     \
      <30   30-60   >60
```

Two keys create three possible ranges; therefore, three children.

---

### Rule 4 - All leaves are at the same depth

A B-Tree is always balanced.

For example

```
              [40 | 70]
             /    |    \
           [20]  [50]  [80]
```

All leaves are on the same level.

This prevents the tree from becoming unnecessarily tall.

---

### Rule 5 - Nodes have minimum and maximum capacities

B-Trees don't allow nodes to contain an arbitrary number of keys.

The number of keys depends on the tree's order or minimum degree, depending on the definition being used.

This restriction is what allows the tree to remain balanced.


---


## 5. How Searching Works

Suppose we have:

```
              [30 | 60]
             /    |    \
           [10]  [40]  [70 | 80]
```

We want to find `70`.

First, examine:

```
[30 | 60]
```

Since:

```
70 > 60
```

We follow the right child.

```
              [30 | 60]
             /    |    \
           [10]  [40]  [70 | 80]
                         ↑
```

We find `70`.

The process is therefore similar to Binary Search Trees, but each node contains multiple keys.

---

## 6. Insertions

When inserting a value:

1. Start at the root.
2. Find the appropriate leaf.
3. Insert the key into sorted order.
4. If the node becomes too large, split it.
5. Promote a key to the parent.
6. Continue splitting upward if necessary.

Example

Suppose we have:

```
        [20 | 40]
```

and the node cannot accept another key.

We insert `30`:

```
        [20 | 30 | 40]
```

If this exceeds the node's maximum capacity, the node is split.

Conceptually:

```  
        [20 | 30 | 40]
```

becomes something like:

```
           [30]
          /    \
       [20]   [40]
```

The middle key is promoted to the parent.

This splitting process is one of the most important ideas in B-Trees.

---

## 7 Node Splitting

Node splitting is what allows B-Trees to remain balanced as they grow.

Imagine:

```
             [50]
            /    \
      [10 | 20] [60 | 70]

```

We insert `30`:

```
           [50]
            /    \
 [10 | 20 | 30] [60 | 70]

```

If the left node is now too large, it can be split.

The middle key moves upward:

```
              [20 | 50]
             /    |    \
          [10]   [30]  [60 | 70]
```

The tree becomes wider rather than deeper.

---

## 8. Deletion

Deletion is more complicated than searching or inserting.

When deleting a key:

1. Find the key.
2. Remove it.
3. Check whether the node still has enough keys.
4. If the node has too few keys, rebalance it.
5. Keys may be borrowed from a sibling.
6. If borrowing is impossible, nodes may be merged.

For example:

```
             [40]
            /    \
        [20]      [60]
```

If deleting `20` causes the left node to become underfilled, the tree may redistribute keys or merge nodes.

The goal is always to preserve the B-Tree's minimum occupancy and balanced structure.

---

## 9. Time Complexity

For a properly balanced B-Tree:

| Operation | Complexity |
| --------- | ---------: |
| Search    |   O(log n) |
| Insert    |   O(log n) |
| Delete    |   O(log n) |
| Traversal |       O(n) |

However, the real advantage of B-Trees isn't simply that they are `O(log n)`

AVL and Red-Black Trees are also O(log n).

The important advantage is:

> B-Trees achieve this with a very small number of tree levels, reducing expensive storage accesses.


---

## 10. Why B-Trees Are Good for Storage

Imagine a database with millions of records.

A database doesn't want to repeatedly access storage like this:

```
Read → node
Read → node
Read → node
Read → node
Read → node
...

```

Instead, it wants each storage access to bring back a large amount of useful information.

A B-Tree node can contain many keys:

```
        [10 | 20 | 30 | 40 | 50 | 60 | 70]
```

One node access can therefore eliminate the need to visit many additional levels.

This is the fundamental reason B-Trees became so important to databases and file systems.

---

## 11. B-Tree vs Binary Search Tree

| Binary Search Tree               | B-Tree                             |
| -------------------------------- | ---------------------------------- |
| Usually one key per node         | Multiple keys per node             |
| At most two children             | Many children                      |
| Can become tall                  | Designed to remain shallow         |
| Good for memory-based structures | Designed for large storage systems |
| Can become unbalanced            | Always balanced                    |
| Fewer keys per node              | Many keys per node                 |


The fundamental difference is:

> BSTs optimize the tree structure around individual nodes. B-Trees optimize the tree around storage access.


---

## 12. B-Tree vs AVL and Red-Black Trees

| AVL                        | Red-Black                  | B-Tree                 |
| -------------------------- | -------------------------- | ---------------------- |
| Binary                     | Binary                     | Multi-way              |
| Strictly balanced          | Approximately balanced     | Balanced               |
| One key per node           | One key per node           | Multiple keys per node |
| Excellent for memory       | Excellent for memory       | Excellent for storage  |
| More rotations             | Fewer rotations            | Uses splitting/merging |
| Common in-memory structure | Common in-memory structure | Databases/file systems |


This gives us an important progression:

```
AVL
 ↓
Keep memory-based search trees balanced

Red-Black
 ↓
Reduce balancing overhead for updates

B-Tree
 ↓
Reduce the number of expensive storage accesses
```

---

## 13. Advatanges

- Always balanced.
- Guaranteed O(log n) search, insertion, and deletion.
- Stores many keys per node.
- Produces very shallow trees.
- Minimizes storage accesses.
- Efficient for very large datasets.
- Well suited to databases and file systems.
- Handles dynamic insertion and deletion efficiently.

---

## 14. Disadvantages

- More complicated to implement than a Binary Search Tree.
- Insertion requires node splitting.
- Deletion requires redistribution or merging.
- Searching within a node requires comparing multiple keys.
- Not usually the first choice for simple in-memory collections.

## 15. Real-World Uses

B-Trees are particularly important in systems that manage large amounts of persistent data.

Examples include:

- Database indexes
- File systems
- Storage engines
- Key-value stores
- Large-scale data systems

Many database technologies use B-Tree-family indexes because they provide efficient searching while minimizing storage I/O.

---

## 16. The Big Picture

The tree structures you've studied are actually telling one continuous story:

```
Binary Search Tree
        ↓
Fast searching
        ↓
But can become unbalanced
        ↓
AVL Tree
        ↓
Strict balancing
        ↓
But balancing updates can be expensive
        ↓
Red-Black Tree
        ↓
Relax balancing to reduce update overhead
        ↓
But trees are still fundamentally binary
        ↓
B-Tree
        ↓
Multiple keys + multiple children
        ↓
Much shorter tree
        ↓
Fewer expensive storage accesses
```
And that's the reason B-Trees exist.

---

# Questions

1. Why does a B-Tree store multiple keys in a node?

> To allow each node to represent multiple values and ranges, making the tree wider and reducing its height.

2. Why are B-Trees particularly useful for databases?

> Because database data is often stored on persistent storage, and B-Trees reduce the number of storage accesses required to find data.

3. Why are all B-Tree leaves at the same depth?

> To guarantee that the tree remains balanced and prevent some searches from becoming much longer than others.

4. What happens when a B-Tree node becomes too large?

> The node is split, and a key is promoted to the parent.

5. What happens when a node becomes too small after deletion?

> The tree can redistribute keys from a sibling or merge nodes to restore the required minimum occupancy.

6. Why isn't O(log n) alone the reason B-Trees are useful?

> Because AVL and Red-Black Trees are also O(log n). B-Trees are valuable because they achieve efficient operations while minimizing expensive storage accesses.

7. What is the main difference between a B-Tree and a Binary Search Tree?

> A Binary Search Tree has at most two children per node, while a B-Tree can have many keys and many children per node.

8. What problem are B-Trees fundamentally solving?

> They reduce the number of expensive storage accesses needed to search and modify large datasets.

