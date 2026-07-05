# Arrays

> 1. ## The Problem
Imagine you're building an application that stores a user's last 10 search queries.

One approach would be to create a separate variable for each search, but this quickly becomes difficult to manage.

Now imagine storing
- 100 student marks
- 1,000 customer names
- 1,000,000 sensor readings

Creating individual variables for each value is impossible to maintain.

We need a way to store **many values of the same type** under a single name while allowing fast access to each value.

This problem led to one of the most fundamental data structures in Computer Science:

**The Array**
---
> ## 2. The Solution
An array stores a collection of elements **contiguously in memory**.
Instead of creating many individual variables, we create one variable that contains multiple values.

```text
Scores

+----+----+----+----+----+
| 80 | 75 | 92 | 61 | 88 |
+----+----+----+----+----+
```

Each element is identified by its **index**.

```text
Index

 0    1    2    3    4
+----+----+----+----+----+
| 80 | 75 | 92 | 61 | 88 |
+----+----+----+----+----+
```
Instead of asking:

> "Where is the value 92?"

We ask:

> "What value is stored at index 2?"

---
> ## 3. How it works

**Contiguous Memory**
The defining characteristics of any array is that all elements are stored **next to each other in memory**.

Imagine memory looks like this:

```text
Address

1000
1004
1008
1012
1016
```
An integer occupies 4 bytes.

An array containing five integers might look like:

```text
Address     Value

1000          80
1004          75
1008          92
1012          61
1016          88
```
Notice there are no gaps.
This contiguous layout is what makes arrays extremely fast.

---
> ## Accessing an element
Suppose we want the value at index 3.
The computer does not start searching from the beginning.
Instead, it calculates the memory address directly.

```
Address = Base Address + (Index × Size of Element)
```
Example:

```
Base Address = 1000
Index = 3
Size = 4 bytes

Address = 1000 + (3 × 4)
Address = 1012
```

The computer immediately jumps to address **1012**.

There is no searching involved.

This is why array access is **O(1)**.

---

> ## Inserting an Element

Suppose we have:
```text
Index

0   1   2   3
+---+---+---+---+
|10 |20 |40 |50 |
+---+---+---+---+
```

Now we want to insert **30** at index 2.

Everything after index 2 must move one position to the right.

```text
Before

10 20 40 50


After

10 20 30 40 50
```

The elements **40** and **50** had to be shifted.

This is why inserting in the middle costs **O(n)**.

---

> ## Deleting an Element

Suppose we remove **20**.
```text
Before

10 20 30 40 50
```

Everything after 20 moves left.

```text
After

10 30 40 50
```

Again, multiple elements must be shifted.

Deleting is also **O(n)**.
---

> ## Searching
There are two common ways to search an array.

### Unsorted Array
The computer checks each element until it finds the target.

```
10 → 20 → 30 → 40 → 50
```
Worst-case complexity:

```
O(n)
```

---

### Sorted array
If the array is sorted, we can use **Binary search**

Instead of checking every element, we repeatedly divide the search space in half.

```
O(log n)
```
We'll explore Binary Search later in the chapter.

---

> # Time Complexity
| Operation | Complexity |
|-----------|------------|
| Access | O(1) |
| Search (Unsorted) | O(n) |
| Search (Binary Search) | O(log n) |
| Insert (End)* | O(1) |
| Insert (Middle) | O(n) |
| Delete | O(n) |

> *Appending to the end assumes there is available space.

> # Static vs Dynamic Arrays
## Static Arrays
The size is fixed when the array is created.

Example:
```
int scores[100];
```

Advantages:
- very fast
- simple memory layout

Disadvantages:
- cannot grow
- wasted memory if not full

---

> ## Dynamic Arrays
Dynamic arrays automatically grow when they become full.

Examples include:

- Java `ArrayList`
- C++ `std::vector`
- Python `list`

When the array becomes full, a larger array is created.

```
Capacity = 4

[1][2][3][4]

↓

Capacity = 8

[1][2][3][4][ ][ ][ ][ ]
```

The old elements are copied into the new array

Although resizing is expensive, it happens infrequently enough that appending remains **amortized O(1)**.
---
> # 4. Real-World Applications
Arrays appear almost everywhere in software engineering because they provide fast, predictable access to data.

## Images
An image is stored as a grid of pixels.

```text
[Red][Blue][Green]
[Red][Red][Blue]
[Black][White][Gray]
```

Each pixel occupies a position in an array.

---

## Audio and Video

A song is stored as millions of audio samples arranged sequentially in an array.
A video is a sequence of frames, each containing arrays of pixel data.
---

##Game Development

Games often store:
- player position
- enemy locations
- map tiles
- animations

using arrays for fast access during rendering.

---

## Databases
Although databases use more advanced data structures internally, arrays are heavily used inside storage engines for buffers, pages, and indexes.

---
## Machine Learning

Neural networks operate on large multidimensional arrays (often called tensors).
Every prediction involves millions or even billions of array operations.

---

> # 5. Advantages and trade-offs

 ## Advantages

**Fast Random Access**
 Any element can be accessed in constant time using its index.

** Cache-friendly **
Because elements are stored contiguously, CPU can efficiently load nearby elements into the cache.
This significantly improves performance.

**Memory efficient**
Arrays store only the elements themselves, with minimal overhead.

**Simple**
Arrays are easy to understand and implement. Many other data structures build upon them.

---
## Trade-offs

**Fixed size (static array)**
The size must be known in advance.


**Expensive Insertions**
Inserting into the middle requires shifting elements.

**Expensive deletions**
Removing an element also requires shifting elements.

**Inefficient Growth**
Growing a static array requires allocating a new block of memory and copying all elements.
Dynamic arrays automate this process but still incur occasional resizing costs.


# Key Takeaways

- Arrays store elements in **contiguous memory**.
- Direct address calculation enables **O(1)** indexed access.
- Insertions and deletions in the middle require shifting elements, resulting in **O(n)** time.
- Dynamic arrays trade occasional resizing costs for flexible growth.
- Arrays are one of the most widely used data structures and serve as the foundation for many higher-level structures and algorithms.

---

 







