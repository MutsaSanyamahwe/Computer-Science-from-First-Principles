# Segment Trees

## 1. The Problem

So far, we have seen trees designed for different kinds of data.

- BST / AVL / Red-Black Trees -> organize values for efficient search.
- B-Trees / B+ Trees -> organize large amounts of data while reducing storage accesses.
- Tries -> organize strings based on their prefixes.

But consider a different problem.

Suppose we have an array:

```
[2, 4, 5, 7, 8, 9]
```

We want to repeatedly ask questions about ranges of the array:

```
What is the sum from index 1 to 4?
What is the minimum from index 2 to 5?
What is the maximum from index 0 to 3?
```

A simple loop works:

```
sum(1, 4)
→ 4 + 5 + 7 + 8
→ 24
```

But what if the array is very large and we perform thousands or millions of these queries?

Scanning every element in the requested range can become expensive.

Now make the problem harder:

```
Query a range
Update an element
Query another range
Update another element
...
```
We need a structure that can efficiently handle both range queries and updates.

---

## 2. The Solution

A Segment Tree is a tree data structure that divides an array into segments (ranges) and stores information about those segments.

Instead of repeatedly scanning the array, we precompute information about different ranges.

For example:

```
Array:

[2, 4, 5, 7, 8, 9]

             [0..5]
            /      \
         [0..2]    [3..5]
         /   \      /   \
      [0..1] [2]  [3..4] [5]
      /  \         /  \
    [0]  [1]     [3]  [4]
```

Each node represents a range of the original array.

The node can store something useful about that range:

- sum
- minimum
- maximum
- greatest common divisor
- or another value that can be combined from smaller ranges.

The key idea is:

> A Segment Tree breaks a large range into smaller precomputed ranges so queries don't have to inspect every element.

---

## 3. Why Divide the Array into Segments?

Suppose we want:

sum(1, 4)

Without a Segment Tree:

4 + 5 + 7 + 8

We inspect four elements.

With a Segment Tree, the requested range can be represented using a small number of existing segments.

For example:

```
[1..1] + [2..2] + [3..4]
```

The tree already knows the sum of `[3..4]`.

So instead of calculating everything from individual elements, we combine precomputed results.

This is the fundamental idea behind Segment Trees.

---

## 4. What does Each Node Store?

A Segment Tree node represents a range and stores information about that range.

For a sum Segment Tree:

```
Array:
[2, 4, 5, 7]

             [0..3] = 18
             /      \
       [0..1] = 6   [2..3] = 12
        /   \        /   \
       2     4      5     7
```

The parent is calculated from its children:

```
6 + 12 = 18
```
For a minimum Segment Tree:

```
             [0..3] = 2
             /      \
        [0..1] = 2  [2..3] = 5
```
The operation changes, but the structure remains similar.

---

## 5. Building the Tree

The tree is built recursively.

Start with the entire array:

```
[0..5]
```

Split it into two halves:

```
[0..2]    [3..5]
```
Then split those:

```
[0..1] [2]    [3..4] [5]
```
Continue until each segment represents a single element.

The leaves contain the original array values.

Then we calculate the parent values from their children.

```
For a sum tree:

             [0..3]
            /      \
         [0..1]   [2..3]
          /  \     /  \
         2    4   5    7
```

```
[0..1] = 2 + 4 = 6
[2..3] = 5 + 7 = 12

[0..3] = 6 + 12 = 18
```

---

## 6. Range Queries

This is where Segment Trees become useful.

Suppose:

```
Array:
[2, 4, 5, 7, 8, 9]
```
We want:

```
sum(1, 4)
```
The requested range is:

```
[4, 5, 7, 8]
```
The Segment Tree examines the relationship between the requested range and each node's range.

There are three important cases.


> Case 1: Completely outside

The node's range does not overlap the query.

Example:

```
Node:  [0..0]
Query: [1..4]
```
Ignore the node.

> Case 2: Completely inside

The node's range is completely covered by the query.

Example:

```
Node:  [3..4]
Query: [1..4]
```

We already have the answer for `[3..4]`.

Use it directly.

> Case 3: Partially overlapping

The node's range overlaps the query but is not completely inside it.

Example:

```
Node:  [0..2]
Query: [1..4]
```
We need to explore its children.

So the query recursively breaks the requested range into segments that the tree already knows about.

---

## 7. Why Range Queries Are Fast

Without a Segment Tree:

```
Range query
→ inspect every element
```

Time:

```
O(n)
```

With a Segment Tree:

```
Range query
→ navigate the tree
→ combine relevant segments
```

Time:

O(log n)

More precisely, the standard Segment Tree range-query complexity is O(log n) for common associative operations when the query decomposes into a logarithmic number of canonical segments.

The important idea is:

> We don't calculate the entire range from scratch. We reuse information already stored in the tree.

---

## 8. Updating a Value

Now suppose:

```
Array:
[2, 4, 5, 7, 8, 9]
```

We change:

```
index 2:
5 → 10
```

We cannot simply change the leaf.

The ancestors that depend on that value must also be updated.

The path looks like:

```
             [0..5]
                ↑
             [0..2]
                ↑
              [2]
```

We update:

```
[2] = 10
```

Then recalculate:

```
[0..2]
```

Then:

```
[0..5]
```

Only the nodes along that path need to change.

Therefore:

```
Point update = O(log n)
```

---

## 9. Why Not Just Recalculate Everything?

Suppose we changed:

```
5 → 10
```

We could rebuild the entire tree.

But that would require:

```
O(n)
```

work.

Instead, the change only affects one path from the leaf to the root.

That path has approximately:

```
log₂(n)
```

levels.

So the update is:

```
O(log n)
```

This is one of the main reasons Segment Trees exist.

---


## 10. Segment Tree vs Prefix Sum

A useful comparison is a prefix sum array.

For:

```
[2, 4, 5, 7, 8]
```

We can precompute:

```
[2, 6, 11, 18, 26]
```

Then a range sum can be answered very quickly.

So why use a Segment Tree?

Because prefix sums are great when the array doesn't change frequently.

If we update:

```
5 → 10
```

many prefix sums after that position must change.

That can require:

```
O(n)
```

work.

A Segment Tree handles the update in:

```
O(log n)
```

So:

> Prefix sums are excellent for static range queries. Segment Trees are useful when range queries and updates happen together.

---

## 11. What Operations Can a Segment Tree Support?

Segment Trees are not limited to sums.

The stored value can represent different operations.

> Sum

```
[2, 4, 5, 7]

sum → 18
```

> Minimum

```
min → 2
```

> Maximum

```
max → 7
```

> GCD

```
gcd(2, 4, 6) → 2
```

The important requirement is that the results from segments can be efficiently combined.

For example:

```
left result + right result
```
for sums.

Or:

```
min(left, right)
```

for minimum queries.

---

## 12 Segment Tree Structure

A Segment Tree is essentially:

```
Array
   ↓
Divide into ranges
   ↓
Store information about each range
   ↓
Combine child information
   ↓
Answer queries using those precomputed ranges
```

Mental model:

> The array contains the data. The Segment Tree contains summaries of ranges of that data.


---

## 13. Complexity

For a standard Segment Tree:

```
| Operation    | Complexity |
| ------------ | ---------: |
| Build        |       O(n) |
| Range query  |   O(log n) |
| Point update |   O(log n) |
| Space        |       O(n) |

```

The important combination is:

```
Query → O(log n)
Update → O(log n)
```

That's what makes Segment Trees useful for dynamic range problems.

---

## 14. Segment Tree vs BST

These structures may both use trees, but they solve different problems.

> BST

Organizes values according to their ordering:

```
smaller ← node → larger
```

Useful for:

```
search
insert
delete
```

> Segment Tree

Organizes ranges of an array:

```
[0..n]
     ↓
[0..mid] [mid+1..n]
```

Useful for:

```
range queries
+
updates
```
The key difference:

> A BST organizes values. A Segment Tree organizes ranges.

---

## 15. Advantages

- Fast range queries.
- Fast point updates.
- Works with many operations such as sum, minimum, maximum, and GCD.
- Handles dynamic arrays where values change.
- Avoids repeatedly scanning large ranges.
- Flexible compared with more specialized structures.


---

## 16. Disadvantages

- More complicated than a simple array.
- Uses additional memory.
- More difficult to implement correctly.
- Overkill for simple arrays with few queries.
- For some problems, prefix sums or Fenwick Trees are simpler and more efficient.

The main trade-off is:

> More complexity and memory in exchange for fast dynamic range queries.

---

## 17. Real-World Applications

Segment Trees are particularly useful when a system repeatedly needs information about changing ranges.

Examples include:

- Competitive programming
- Dynamic range statistics
- Scheduling problems
- Interval/range calculations
- Query-heavy numerical data
- Computational geometry
- Maintaining minimum/maximum values over changing ranges

They are especially useful when the pattern looks like:

```
update
query
update
query
query
update
...
```

---

## 19. Big Picture

We can now see how the tree structures we've studied solve increasingly different problems:

```
Binary Tree
     ↓
BST
     ↓
AVL / Red-Black Tree
     ↓
B-Tree
     ↓
B+ Tree
     ↓
Trie
     ↓
Segment Tree
```

The important shift is:

```
BST
→ organize values

B-Tree / B+ Tree
→ organize large amounts of storage-oriented data

Trie
→ organize strings and prefixes

Segment Tree
→ organize ranges of an array

```

The fundamental idea of a Segment Tree is:

> Precompute information about ranges so that queries and updates can be performed without repeatedly scanning the entire array.

