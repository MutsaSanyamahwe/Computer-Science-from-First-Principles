# Fenwick Trees (Binary Indexed Trees)

A Fenwick Tree, also known as a **Binary Indexed Tree (BIT)**, is a compact data structure that efficiently supports **prefix-sum queries** and **point updates**.

## 1. The Problem

In the previous chapter, we learned about Segment Trees, which help us answer range queries and update array elements efficiently.

Consider this array:

```
[2, 4, 5, 7, 8, 9]
```

Suppose we repeatedly ask:

- What is the sum of the first four elements?
- What is the sum between two indices?
- What happens to the sum when one element changes?

A simple approach is to calculate each sum by scanning the array. But as the array grows and queries become more frequent, repeatedly scanning elements becomes expensive.

We could use a Segment Tree. However, Segment Trees are relatively complex and support a wide range of operations that we might not need.

**What if our main concern is efficient prefix sums and updates, using a simpler structure?**

We need a way to store partial sums so that we can combine them without examining every element.

## 2. The Solution

A Fenwick Tree stores partial sums of an array in a compact structure, allowing us to calculate prefix sums without scanning every element.

For a standard Fenwick Tree supporting sums:

| Operation  | Complexity |
| ---------- | ---------- |
| Prefix sum | O(log n)   |
| Point update | O(log n) |
| Space      | O(n)       |

The key idea is that each position stores the sum of a particular range of elements. These ranges are determined by the **binary representation of the position's index**.

> A Fenwick Tree uses binary arithmetic to determine which partial sums to store and combine.

## 3. Why Is It Called a Binary Indexed Tree?

A Fenwick Tree is closely connected to the binary representation of array indices.

Consider the number 12:

```
12 in decimal = 1100 in binary
```

A Fenwick Tree uses a bit-manipulation operation called the **least significant bit (LSB)** to determine the size of the range represented by an index.

For a positive integer `i`:

```
lowbit(i) = i & (-i)
```

Here, `&` is the bitwise AND operator.

For example:

```
i = 12
Binary: 1100

lowbit(12) = 4
```

The Fenwick Tree entry at index 12 stores the sum of the last four elements ending at that index. This means it represents the range `[9, 10, 11, 12]` when using one-based indexing.

You do not need to memorize every binary pattern immediately. First understand the purpose: **the index tells us how large a range each entry represents.**

## 4. The Core Idea: Store Partial Sums

Suppose we have this array:

```
Index:  1  2  3  4  5  6  7  8
Value:  2  4  5  7  8  9  3  6
```

A normal array stores each individual value. A Fenwick Tree stores partial sums over ranges:

| Index | Range represented | Stored sum |
| :---: | :---------------: | :--------: |
| 1     | [1..1]            | 2          |
| 2     | [1..2]            | 6          |
| 3     | [3..3]            | 5          |
| 4     | [1..4]            | 18         |
| 5     | [5..5]            | 8          |
| 6     | [5..6]            | 17         |
| 7     | [7..7]            | 3          |
| 8     | [1..8]            | 44         |

Notice the pattern:

- Index 1 represents 1 element.
- Index 2 represents 2 elements.
- Index 4 represents 4 elements.
- Index 8 represents 8 elements.
- Index 6 represents 2 elements, from index 5 to index 6.

These range sizes are determined by `lowbit(index)`.

For a one-based Fenwick Tree, the entry at index `i` stores:

```
tree[i] = a[i - lowbit(i) + 1] + ... + a[i]
```

In plain English: *start at the current index, count backward by the range size, and store the sum of that range.*

## 5. How a Prefix Sum Works

Suppose we want the sum of the first seven elements:

```
[2, 4, 5, 7, 8, 9, 3]
```

The answer is `2 + 4 + 5 + 7 + 8 + 9 + 3 = 38`.

A Fenwick Tree does not need to visit every element. Instead, it combines stored ranges.

**Step 1.** Start at index 7:

```
Index 7 → represents [7..7] → sum = 3
```

Subtract `lowbit(7)`, which is 1: `7 - 1 = 6`

**Step 2.** At index 6:

```
Index 6 → represents [5..6] → sum = 17
```

Subtract `lowbit(6)`, which is 2: `6 - 2 = 4`

**Step 3.** At index 4:

```
Index 4 → represents [1..4] → sum = 18
```

Subtract `lowbit(4)`, which is 4: `4 - 4 = 0`

We stop. Now combine the stored sums:

```
3 + 17 + 18 = 38
```

We calculated the prefix sum using only **three entries** rather than seven individual values.

### The query process

```
Start at the requested index
          ↓
Add the stored partial sum
          ↓
Subtract lowbit(index)
          ↓
Repeat until index = 0
```

The query takes **O(log n)** time.

## 6. Why Does Binary Arithmetic Help?

The index determines how many elements its entry summarizes.

When calculating a prefix sum, subtracting the least significant set bit moves us backward to the next uncovered section.

For example:

```
7 → 6 → 4 → 0
```

The ranges are:

```
[7..7]
[5..6]
[1..4]
```

Together, they cover every index from 1 through 7 exactly once.

> Fenwick Trees work because binary indices let us decompose a prefix into a small number of non-overlapping ranges.

## 7. Updating a Value

Now suppose index 3 changes:

```
Old value: 5
New value: 10
```

The difference is `10 - 5 = 5`.

We need to add 5 to every Fenwick Tree entry whose stored range contains index 3.

Starting at index 3, set `tree[3] += 5`, then move forward using:

```
index = index + lowbit(index)
```

The sequence is:

```
3 → 4 → 8 → 16 → ...
```

We stop when the index exceeds the array's size. For an array of length 8, we update `tree[3]`, `tree[4]`, and `tree[8]`.

Why these entries?

- `tree[3]` represents `[3..3]`.
- `tree[4]` represents `[1..4]`.
- `tree[8]` represents `[1..8]`.

All three ranges contain index 3, so each stored sum must increase by 5 to remain correct.

### The update process

```
Start at the updated index
          ↓
Add the change to that entry
          ↓
Add lowbit(index) to the index
          ↓
Repeat until outside the array
```

This takes **O(log n)** time.

> **Important:** This update procedure assumes we know the difference between the new and old values. It works naturally for addition-based Fenwick Trees.

## 8. Why Not Just Use Prefix Sums?

Prefix sums are a simple way to answer range-sum queries. For the array `[2, 4, 5, 7, 8]` we can build `[2, 6, 11, 18, 26]`.

The sum from index 2 through index 4 (zero-based) can be calculated by subtracting two prefix sums. However, if one array value changes, many entries in the prefix-sum array may need updating.

| Operation    | Prefix sums | Fenwick Tree |
| ------------ | :---------: | :----------: |
| Build        | O(n)        | O(n)         |
| Prefix sum   | O(1)        | O(log n)     |
| Point update | O(n)        | O(log n)     |
| Space        | O(n)        | O(n)         |

The trade-off:

- Prefix sums provide faster queries when the data rarely changes.
- Fenwick Trees support frequent updates without rebuilding all prefix sums.

## 9. Fenwick Tree vs Segment Tree

Both structures support efficient range-related queries and updates, but they are designed with different priorities.

| Feature      | Fenwick Tree                                            | Segment Tree                                    |
| ------------ | ------------------------------------------------------- | ----------------------------------------------- |
| Main idea    | Store overlapping partial sums determined by binary indices | Build a hierarchy of array ranges           |
| Prefix sum   | O(log n)                                                | O(log n)                                        |
| Point update | O(log n)                                                | O(log n)                                        |
| Range sum    | O(log n)                                                | O(log n)                                        |
| Memory       | O(n)                                                    | Usually O(n), often with a larger constant      |
| Implementation | Usually simpler                                       | Usually more complex                            |
| Flexibility  | Best suited to supported operations such as sums        | Supports a wider variety of range operations    |

A Fenwick Tree is not simply a smaller Segment Tree. It organizes partial sums differently and has different capabilities.

A standard sum-based Fenwick Tree is particularly convenient for addition and prefix sums. A Segment Tree is generally more flexible for operations such as range minimum or maximum, especially when updates are involved.

> Fenwick Trees prioritize simplicity and efficient prefix sums. Segment Trees prioritize flexibility over ranges.

## 10. Why Is One-Based Indexing Common?

Fenwick Trees are usually explained using indices starting at 1, because `lowbit(index)` is used to determine each entry's range size and navigate between entries.

With one-based indexing:

```
lowbit(1) = 1
lowbit(2) = 2
lowbit(3) = 1
lowbit(4) = 4
lowbit(5) = 1
lowbit(6) = 2
lowbit(7) = 1
lowbit(8) = 8
```

The query and update algorithms rely on these values.

Most programming languages use zero-based arrays, so implementations often allocate an array of size `n + 1` and leave index 0 unused. This is a practical implementation detail, not a change to the underlying concept.

## 11. Complexity

For a standard Fenwick Tree:

| Operation  | Complexity                      |
| ---------- | ------------------------------- |
| Build      | O(n) with efficient construction |
| Prefix sum | O(log n)                        |
| Point update | O(log n)                      |
| Range sum  | O(log n)                        |
| Space      | O(n)                            |

A range sum can be calculated using two prefix sums:

```
sum(l, r) = prefix(r) - prefix(l - 1)
```

This formula assumes one-based indexing. The answer comes from subtracting the sum before the requested range from the sum through its final element.

## 12. Advantages

- Efficient prefix-sum queries.
- Efficient point updates.
- Compact O(n) storage.
- Usually easier to implement than a Segment Tree.
- Useful for dynamic cumulative sums.
- Binary arithmetic provides a predictable way to navigate stored ranges.

## 13. Disadvantages

- Less flexible than a Segment Tree for many types of range operations.
- The bit-manipulation logic can initially be confusing.
- The standard sum-based version works most naturally with additive updates.
- The structure is less intuitive to visualize than a conventional tree.
- Range updates and more advanced operations require additional techniques.

The main trade-off:

> A Fenwick Tree sacrifices some flexibility to provide a compact, efficient way to maintain cumulative information.

## 14. Real-World Applications

Fenwick Trees are particularly useful when a system needs to maintain cumulative values as data changes. Examples include:

- Dynamic prefix sums.
- Frequency tables and cumulative frequencies.
- Counting how many values fall below a given rank.
- Inversion counting in arrays.
- Order-statistics problems when paired with suitable frequency representations.
- Competitive programming problems involving frequent point updates and range sums.

For example, suppose we maintain the frequency of different scores. A Fenwick Tree can efficiently answer questions such as *"How many scores are less than or equal to 50?"* by storing frequencies and querying their prefix sum, without scanning the entire frequency table.

## 15. Big Picture

Let's connect this to the previous structures:

```
BST
 ↓
Organize values by ordering

B-Tree / B+ Tree
 ↓
Organize data for efficient storage access

Trie
 ↓
Organize strings by shared prefixes

Segment Tree
 ↓
Store summaries of ranges in a hierarchy

Fenwick Tree
 ↓
Store partial sums using binary-indexed ranges
```

Segment Trees and Fenwick Trees address similar problems, but they approach them differently. A Segment Tree explicitly represents a hierarchy of ranges. A Fenwick Tree stores partial sums at indexed positions and uses binary arithmetic to determine which ranges to combine.

> The fundamental idea: a Fenwick Tree uses the binary structure of indices to maintain cumulative sums efficiently, even when individual values change.

### Mental model

> *"Each index stores a partial sum. Use `lowbit` to jump backward for queries and forward for updates."*

---

## Review Questions

1. What problem does a Fenwick Tree solve?
2. Why is it also called a Binary Indexed Tree?
3. What information does each entry store?
4. What does `lowbit(i)` calculate?
5. Why is one-based indexing commonly used?
6. How does a Fenwick Tree calculate a prefix sum?
7. Why does a prefix query repeatedly subtract `lowbit(index)`?
8. How does a point update work?
9. Why does an update repeatedly add `lowbit(index)`?
10. What is the difference between a Fenwick Tree and prefix sums?
11. What is the difference between a Fenwick Tree and a Segment Tree?
12. What is the time complexity of a prefix-sum query?
13. What is the time complexity of a point update?
14. How can a range sum be calculated using two prefix sums?
15. What is the main advantage of Fenwick Trees?
16. What is their main limitation?
17. How can a Fenwick Tree help count values below a particular rank?
18. What is the fundamental idea behind a Fenwick Tree?
