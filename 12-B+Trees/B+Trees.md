# B+ Trees

## 1. The Problem

B-Trees solved an important problem.

Large datasets are often stored on secondary storage such as:

- SSDs
- Hard drives
- Database storage
- File systems

Accessing secondary storage is much more expensive than accessing data already in memory.

B-Trees address this by:

- Storing multiple keys per node
- Supporting multiple children per node
- Keeping the tree balanced
- Keeping the tree relatively shallow

This reduces the number of expensive storage accesses.

However, B-Trees have another problem.

Consider a database query such as:

```SQL
SELECT *
FROM users
WHERE age >= 20
AND age <= 30;
```

This is a range query.

We don't just want to find one value.

We want to find many consecutive values.

A B-Tree can perform this operation, but its structure is not specifically optimized for scanning through a sequence of neighbouring records.

We need a structure that can:

- Quickly find where a range begins.
- Keep records ordered
- Efficiently move through neighbouring records
- Still maintain the shallow structure of a B-Tree

This leads to the B+ Tree

---

## 2. The Solution


A B+ Tree is a variation of a B-Tree designed to make ordered and range-based access more efficient.

The key idea is:

> Internal nodes are used for navigation, while the actual records are stored at the leaf level.


For example:

```
                 [30 | 60]
                /    |    \
               /     |     \
              ↓      ↓      ↓

          [10 | 20] [30 | 40 | 50] [60 | 70 | 80]
```

The upper levels help us determine where to search.

The leaves contain the actual data or references to the data.

This creates a clear separation:

```
Internal nodes
      ↓
Navigation / Index

Leaf nodes
      ↓
Actual records
```


---


## 3. The Key Difference

In a traditional B-Tree, records can be stored throughout the tree.

For example:

```
                [30 | 60]
               /    |    \
          [10,20] [40,50] [70,80]
```

A key may be found in an internal node.

In a B+ Tree, the actual records are stored at the leaves:

```
                [30 | 60]
               /    |    \
              ↓     ↓      ↓

        [10,20] [30,40,50] [60,70,80]
```


The internal keys act primarily as routing information.

They tell us which child contains the values we're looking for.

---

## 4. Why Move the Data to the Leaves?

This design provides an important advantage.

If internal nodes don't need to store the actual records, they can focus on storing:

```
keys + child pointers
```

This allows internal nodes to contain more routing information.

For example:

```
             [10 | 20 | 30 | 40 | 50 | 60 | 70]
```

More keys per internal node means:

```
More keys
    ↓
More children
    ↓
Higher branching factor
    ↓
Fewer levels
    ↓
Fewer storage accesses
```

This builds directly on the reason B-Trees use multiple keys per node.

---

## 5. The Most Important Feature: Linked Leaves

The biggest difference between a B-Tree and a B+ Tree is not simply that records are stored in leaves.

It is that leaf nodes are linked together.

For example;

```
                 [30 | 60]
                /    |    \
               ↓     ↓      ↓

        [10,20] → [30,40,50] → [60,70,80] → [90,100]
```

Each leaf contains a pointer to the next leaf.


This creates an ordered sequence of all the records.

Think of it as two ways of moving through the tree:

```
                 ROOT
                  ↓
             ↓    ↓    ↓
            LEAF → LEAF → LEAF → LEAF
```

The tree provides vertical navigation.

The leaf links provide horizontal traversal.

> Search vertically. Scan horizontally.


---

## 6. How Searching Works

Suppose we have:

```
                 ROOT
                  ↓
             ↓    ↓    ↓
            LEAF → LEAF → LEAF → LEAF
```

We want to find `50`

First, examine the root:

```
[30 | 60]
```

Since:

```
30 < 50 < 60
```

we follow the middle child.

```
                 [30 | 60]
                      |
                      ↓
                 [30,40,50]
```

We reach the leaf and find `50`.

The important difference from a B-Tree is that the search ultimately reaches the leaf containing the record.

---

## 7. Range Queries

This is where B+Trees become particularly useful.

Suppose we want:

```SQL
WHERE age BETWEEN 30 AND 80;
```

We first search for `30`.

```
                 [30 | 60]
                      |
                      ↓
                 [30,40,50]
```

Now we don't need to start from the root again to find `40`, `50`, `60`, and so on.

We simply follow the leaf links:

```
[30,40,50]
      ↓
[60,70,80]
      ↓
[90,100]
```

We stop when we pass `80`.

The process is therefore:


```
Find beginning of range
          ↓
      Scan leaves
          ↓
      Stop at end
```


This makes B+ Trees particularly useful for range queries.

---

## 8 Point Queries vs Range Queries

A B+ Tree can efficiently support both.

### Point Query

Find one specific value:

```SQL
WHERE id = 500;
```

The tree navigates to the appropriate leaf:

```
Root
 ↓
Internal node
 ↓
Leaf
 ↓
500
```

### Range query

Find multiple values:

```SQL
WHERE id BETWEEN 500 AND 600;
```

The tree:

```
1. Finds 500
        ↓
2. Reaches the appropriate leaf
        ↓
3. Follows the leaf links
        ↓
4. Continues until 600
```

This is one of the main reasons for the B+ Tree design.

---

## 9. Insertions

Insertion follows a similar process to a B-Tree.

> Step 1

Start at the root.

> Step 2

Follow the appropriate child until reaching a leaf.

> Step 3

Insert the key into sorted order.

> Step 4

Check whether the leaf has exceeded its capacity.

> Step 5

If necessary, split the leaf.

> Step 6

Update the parent with the appropriate separator key.

> Step 7

If the parent becomes too large, split it as well.

The process can continue toward the root.

---

## 10. Leaf Splitting

Suppose a leaf currently contains:

```
[10 | 20 | 30 | 40]

```
and another value is inserted:

```
50
```

If the node is now too large:

```
[10 | 20 | 30 | 40 | 50]
```

we split it.

Conceptually:

```
[10 | 20] → [30 | 40 | 50]
```

The two leaves remain connected.

The parent must now be updated so that it knows about the new leaf.

For example:
```
                 [30]
                /    \
               ↓      ↓

          [10,20] → [30,40,50]
```

The leaf-level linked structure is preserved.

---

## 11. Internal Node Splitting

Internal nodes can also become too large.

For example:

```
[10 | 20 | 30 | 40 | 50]
```

may need to be split.

The split creates additional internal nodes, and a separator key is propagated upward.

If the root becomes too large, it can also split.

A new root is created.

This allows the tree to grow while maintaining its balanced structure.

---

## 12. B+ Trees Remain Balanced

Like B-Trees, B+ Trees maintain the rule:

> All leaves are at the same depth.

For example:

```
                 [30 | 60]
                /    |    \
               ↓     ↓      ↓

             Leaf   Leaf    Leaf
```
No leaf can be significantly deeper than another.

This guarantees predictable search performance.

---

## 13. Complexity

For a balanced B+ Tree containing `n` records:

| Operation   |   Complexity |
| ----------- | -----------: |
| Search      |     O(log n) |
| Insert      |     O(log n) |
| Delete      |     O(log n) |
| Traversal   |         O(n) |
| Range query | O(log n + k) |

where `k` is the number of records returned by the range query.

For example:

```
Find first record
      ↓
O(log n)

Scan k records
      ↓
O(k)

Total
      ↓
O(log n + k)

```
The important point is that the tree efficiently finds the starting point, while the linked leaves efficiently handle the sequential scan.

---

## 14. B-Tree vs B+ Tree

| **B-Tree**                           | **B+ Tree**                                             |
| ------------------------------------ | ------------------------------------------------------- |
| Multiple keys per node               | Multiple keys per node                                  |
| Multiple children                    | Multiple children                                       |
| Balanced                             | Balanced                                                |
| Records can appear in internal nodes | Records stored at leaves                                |
| Leaves don't need to be linked       | Leaves are linked                                       |
| Good for search                      | Good for search                                         |
| Supports range queries               | Particularly efficient for range queries                |
| Internal nodes can contain records   | Internal nodes primarily contain navigation information |

The fundamental difference is:

> A B-Tree distributes records throughout the tree, while a B+ Tree concentrates records at the leaves and links those leaves together.


---

## 15. Advantages

- Always balanced.
- O(log n) search, insertion, and deletion.
- Stores many keys per node.
- Produces shallow trees.
- Minimizes expensive storage accesses.
- Keeps records ordered at the leaf level.
- Efficient for range queries.
- Efficient for sequential traversal.
- Well suited to databases and storage systems.

---

## 16. Disadvantages

- More complicated than simpler search trees.
- Insertions can require leaf and internal node splitting.
- Deletions can require redistribution or merging.
- Requires additional pointers between leaves.
- Maintaining the linked leaf structure adds implementation complexity.
- Not always necessary for simple in-memory collections.

---

## 17. Real-World Uses

B+ Trees are particularly useful in systems that need:

- Persistent storage
- Ordered data
- Efficient point lookups
- Efficient range queries
- Sequential access

Common applications include:

- Database indexes
- File systems
- Storage engines
- Key-value stores
- Large-scale persistent data systems

---

## 18. The Big Picture

```
Binary Search Tree
        ↓
Fast searching
        ↓
Can become unbalanced
        ↓
AVL Tree
        ↓
Strict balancing
        ↓
Red-Black Tree
        ↓
Reduce balancing overhead
        ↓
But still binary
        ↓
B-Tree
        ↓
Multiple keys + multiple children
        ↓
Shorter tree
        ↓
Fewer storage accesses
        ↓
B+ Tree
        ↓
Records concentrated at leaves
        ↓
Leaves linked together
        ↓
Efficient range scanning
```

# Questions

1. Why were B+ Trees developed from the B-Tree idea?

> To improve how ordered data and range queries are accessed while retaining the shallow, storage-efficient structure of B-Trees.

2. Where are the actual records stored in a B+ Tree?

> At the leaf level.

3. What are internal nodes primarily used for?

> Navigation. They contain keys and child pointers that direct searches toward the appropriate leaf.

4. Why are B+ Tree leaves linked?

> So that once a search reaches the beginning of a range, neighbouring records can be accessed sequentially without repeatedly traversing the tree.

5. What is the main advantage of linked leaves?

> Efficient range queries and sequential traversal.


6. What happens when a leaf becomes too large?

> It is split into multiple leaves, and the parent is updated with the appropriate separator information.

7. Are B+ Trees balanced?

> Yes. All leaves remain at the same depth.

8. What is the range-query complexity?

> O(log n + k), where k is the number of records returned.

9. What is the main difference between a B-Tree and a B+ Tree?

> B-Trees can store records throughout the tree, while B+ Trees store records at the leaves and link those leaves together.

10. What is the mental model for a B+ Tree?

> Search vertically. Scan horizontally.

11. Why don't we simply use a hash table?

> Hash tables are excellent for exact lookups, but they do not naturally maintain sorted order or efficiently support range queries.

12. What problem does the B+ Tree ultimately solve?

> It provides a shallow, storage-efficient search structure while making ordered and range-based access to large datasets efficient.
