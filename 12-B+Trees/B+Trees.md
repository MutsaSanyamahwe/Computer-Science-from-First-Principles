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


