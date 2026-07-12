# Hash Functions

## 1. The Problem

Imagine you have a collection of one million usernames.

```text
Alice
Bob
Charlie
David
...
```

Now suppose you want to check whether the username **Mutsa** exists.

One approach is to search every username one by one.

```
Alice x
Bob x
Charlie x
...
Mutsa [found]
```

In the worst case, you may have to inspect every element.

For large datasets, this becomes inefficient.

What we need is a way to locate data **without searching the entire collection**.

---

## 2. The Solution

A **hash function** transforms data of any size into a fixed-size value called a **hash* (or **hash code**).

Instead of searching for data directly, we compute its hash.

```text
"Mutsa"

↓

Hash Function

↓

842913
```

This hash value can then be used to determine where the data should be stored or found.

Rather than searching through every element, we compute the hash and jump directly to the expected location.

---

## 3. How It Works

A hash function accepts an input called a **key**.

Examples:

```text
"apple"

"banana"

"user@email.com"

12345
```

Each input is transformed into a hash value.

```text
"apple"   → 734829

"banana"  → 183741

"orange"  → 492018
```

The same input always produces the same hash.
```text
Hash("apple")

↓

734829
```

Every time.

---

## 4. Desirable Properties of a Good Hash Function

A good hash function should have several important properties.

### Deterministic

The same input always produces the same output.

```text
Hash("Mutsa")

↓

12345

Hash("Mutsa")

↓

12345
```

---


### Fast

Computing the hash should be significantly faster than searching through the data.

---

### Uniform distribution

Hash values should be separated evenly.

Good distribution:

```text
1
18
42
67
81
95
```

Poor distribution:

```text
1
2
3
4
999999
```

Uneven distribution causes too many values to end up in the same location.

---

### Minimize Collisions

Different inputs should ideally produce different hash values.

  Good:
```text
Alice

↓

124

Bob

↓

821
```

Poor:
```text
Alice

↓

500

Bob

↓

500
```

When two different inputs produce the same hash value, a **collision** occurs.

---

## 5. What Are Collisions?

A collision happens when two different inputs generate the same hash.

```text
Alice

↓

205

Bob

↓

205
```

Since two pieces of data cannot occupy the exact same location in a hash table, collisions must be handled.

Common collision handling techniques include:

- Separate Chaining
- Open Addressing

These are covered in the Hash Tables chapter.

---

## 6. Time Complexity

Computing a hash value is generally:

| Operation | Complexity |
|-----------|------------|
| Compute Hash | O(1) |

The exact complexity depends on the algorithm and the size of the key, but for typical applications it is considered constant time.

---

## 7. Advantages

- Extremely fast lookups
- Constant-time indexing in many cases.
- Foundation of many modern data structures.

---

## 8. Disadvantages
- Collisions are unavoidable.
- Poor hash functions lead to poor performance.
- Good hash function design can be challenging..

---

## 9. Real-World Applications

Hash functions are used everywhere in software engineering.

### Hash Tables

Hash values determine where data is stored.

---

### Databases

Many databases use hashing for indexes and lookups.

---

### Caching

Systems like Redis use hashing to locate cached data efficiently.

---

### Password Storage

Passwords are stored as hashes rather than plain text.


- Enables efficient searching without scanning every element.

Instead of storing:

```text
password123
```

Applications store something like:

```text
5e884898da...
```

This improves security because the original password cannot be directly read from the database.

---

### Distributed Systems

Hashing helps distribute data across multiple servers.

This concept leads to **Consistent Hashing**, which is widely used in scalable systems.

---

### Checksums and Data Integrity

Hashes can detect whether files or messages have been modified.

If the computed hash changes, the data has changed.

---

## 10. Why System Designers Care

Hash functions are one of the most fundamental tools in system design.

They are used to build:

- Hash Tables
- Hash Maos
- Distributed caches
- Database indexes
- Load balancing algorithms
- Consistent Hashing
- Content delivery systems
- Deduplication systems

- Understanding hash functions makes it much easier to understand how large-scale systems locate and distribute data efficiently.

---

## 11. Key Takeaways

- A hash function transforms data into a fixed-size hash value.
- The same input always produces the same output.
- Good hash functions distribute values evenly.
- Collisions occur when different inputs produce the same hash.
- Hash functions are the foundation of hash tables, databases, caching, and distributed systems.

---

# Questions

1. Why do we use hash functions?

> To locate data quickly without searching every element.

---

2. What is a hash value?

> The output produced by a hash function.

---

3. What is a collision?

> When two different inputs produce the same hash value.

---

4. Why should hash values be evenly distributed?

> To reduce collisions and improve lookup performance.

---

5. Why can't collisions be completely avoided?

> Because an unlimited number of possible inputs are mapped into a limited range of hash values.

---

6. Why are hash functions important for hash tables?

> They determine where keys should be stored and found.

---

7. What happens after a collision?

> The data structure must use a collision resolution strategy, such as separate chaining or open addressing.

---

8. Why is a good hash function critical for system performance?

> Poor distribution increases collisions, making lookups slower.

---

9. Why are passwords hashed instead of encrypted?

> Hashing is a one-way operation designed for verification, while encryption is reversible with the correct key.

---

10. How do distributed systems use hash functions?

> They use hashes to decide which server should store a piece of data.

---

11. What is the relationship between hash functions and consistent hashing?

> Consistent hashing uses hash functions to distribute data evenly across changing sets of servers while minimizing data movement.

---

12. Name five systems that rely heavily on hash functions.

> Hash tables, databases, caches, distributed systems, and password storage.

---

# Whats Next?
Hash functions answer one question: How do we convert a key into a location?
The next chapter, Hash Tables, answers the next question: Once we have that location, how do we actually store and retrieve data efficiently—even when collisions occur?
