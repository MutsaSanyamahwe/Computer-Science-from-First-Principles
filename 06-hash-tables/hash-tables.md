# Hash Tables

## 1. The Problem

Imagine you have information about millions of users.

```
Mutsa     → Developer

Alice     → Designer

John      → Manager
```

If you stored this in an array or linked list, finding "John" would require checking elements one by one.

```
Mutsa

↓

Alice

↓

John ✓
```

For large datasets, searching becomes slow.

We need a way to find data almost instantly without searching every element.

---

## 2. The Solution

A hash table stores data as key-value pairs.

Instead of searching every element, it computes where the data should be stored using a hash function.

```
Key

"John"

↓

Hash Function

↓

Index 7

↓

Table[7]

```

Instead of asking:
> Where is John?

The hash function tells us:
> John belongs in bucket 7.


---

## 3. Key Concepts

A hash table has three important parts.

###  Key
The unique identifier.

Examples:
```
Username

Email

Product ID

Order Number
```

---


###  VAalue
The information associated with the key.

```
Email

↓

User Profile
```

---

### Hash Function

A function that converts a key into an array index.

```
"Mutsa"

↓

Hash Function

↓

5
```

The goal is to spread data evenly across the table.

---

## 4. How It Works

Suppose our table has ten buckets.

```
0

1

2

3

4

5

6

7

8

9
```

Insert:

```
Mutsa
```

Hash function returns:

```
5
```

Store:

```
5 → Mutsa
```

Insert:

```
Alice
```

Hash returns:


```
3
```

Store:

```
2 -> Alice
```

Searching later:

```
Find Alice

↓

Hash("Alice")

↓

2

↓

Found immediately
```

No need to search every entry.

---

## 5. Hash Collisions

Sometimes two different keys produce the same index.

Example:

```
Hash("Alice") = 2

Hash("John") = 2
```

This is called a collision.

Collisions are unavoidable because there are usually far more possible keys than buckets.

The goal is to handle collisions efficiently.

---

## 6. Collision Resolution

### Separate Chaining
Each bucket stores a linked list (or another collection).

```
Bucket 2

↓

Alice

↓

John

↓

David
```

Searching only checks the small chain instead of the entire table.

---

### Open Addressing

Instead of storing multiple items in one bucket, the table searches for another empty bucket.

Example:

```
2 occupied

↓

Try 3

↓

Occupied

↓

Try 4

↓

Empty

↓

Store here


```

Common strategies include:
- Linear probing
- Quadratic probing
- Double hashing

---

## 7. Time Complexity

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |


The worst case occurs when many keys collide, but with a good hash function and proper resizing, average performance is close to O(1).

---

## 8. Load Factor

The load factor measures how full the hash table is.

```
Load Factor = Number of Entries / Number of Buckets
```

Example:

```
80 entries

100 buckets

Load Factor = 0.8
```

As the load factor increases:
- More collisions occur.
- Searches become slower.

---

## 9. Resizing (Rehashing)

When the load factor becomes too high, the table grows.

Examples:

Before

```
10 buckets
```

After

```
20 buckets
```

Every key must be hashed again because the bucket count has changed.

This process is called rehashing.

Although rehashing is expensive, it happens infrequently. This is why inserts remain amortized O(1).

---

## 10. Advantages

- Extremely fast lookups
- Fast insertions
- Fast deletions
- Ideal for key-value data.
- Scales well for large datasets.

---

## 11. Disadvantages

- No ordering of keys
- Performance depends on a good hash function.
- Collisions can reduce performance.
- Uses more memory than some other structures.

---

## 12. Real-World Uses

Hash tables are everywhere.

**Dictionaries/Maps**

```Python
user = {
    "name": "Mutsa",
    "age": 24
}
```

---

**Caches**

```
User ID

↓

Cached Profile
```

Redis and Memcached use hash-based lookups internally for fast access.

---

**Database indexes**

Some databases use hash indexes for fast equality searches.

Example:

```SQL
SELECT * FROM Users
WHERE Email = "john@gmail.com";
```

---

**Password Storage**

Passwords aren't stored directly.

Instead, systems store cryptographic hashes of passwords. While these use hash functions, they serve a different purpose (security rather than indexing).

---

**DNS**
A DNS resolver can use hash tables internally to cache domain name lookups.

---

**Compilers**

Compilers often store variables, functions, and symbols in hash tables for quick lookup.

---

## 13. Why System Designers Care

Hash tables are foundational to many high-performance systems.

Examples include:

- In-memory caches (Redis, Memcached)
- Session stores
- API rate limiters
- Load balancer session affinity
- DNS caches
- Database hash indexes
- Hash-based sharding (which leads into consistent hashing)

Many distributed systems rely on the idea of mapping keys quickly and efficiently.

---

## 14. Hash Tables vs Arrays

| Feature         | Array | Hash Table     |
| --------------- | ----- | -------------- |
| Lookup by index | O(1)  | N/A            |
| Lookup by key   | O(n)  | O(1) average   |
| Ordered         | Yes   | No (generally) |
| Memory overhead | Low   | Higher         |


---

## 15. Hash Table vs Linked List

| Feature           | Linked List | Hash Table   |
| ----------------- | ----------- | ------------ |
| Search            | O(n)        | O(1) average |
| Insert            | O(1)        | O(1) average |
| Delete            | O(n)        | O(1) average |
| Ordered traversal | Yes         | No           |


---

## 16. Hash Maps

A **Hash Map** is a concrete implementation of a hash table that stores data as key-value pairs.

When a key-value pair is added, the hash map uses a hash function to determine where the data should be stored. Later, when the same key is used, it is hashed again to locate the associated value quickly.

Most programming languages provide built-in hash map implementations, including:

- Java `HashMap<K, V>`
- Python `dict`
- Javascript: `Map`
- C# `Dictionary<TKey, TValue`
- Go: `map[K]V`

In practice, the terms hash table and hash map are often used interchangeably. However, it's helpful to think of a hash table as the underlying computer science concept, while a hash map is the implementation that developers use in their programs.



---

## 17. Hash Maps vs Hash Tables

Although the terms are often used interchangeably, there is a subtle difference.

| Hash Table                                                               | Hash Map                                                                                 |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| The underlying data structure that stores key-value pairs using hashing. | A concrete implementation of a hash table provided by a programming language or library. |
| A computer science concept.                                              | A programming language data structure.                                                   |
| Describes *how* key-value storage works.                                 | Describes *how developers use* that concept in code.                                     |

---

## 18. Key Takeaways
- A hash table stores key-value pairs.
- A hash function maps keys to bucket indices.
- Hash tables provide O(1) average lookup, insertion, and deletion.
- Collisions are expected and handled using techniques like separate chaining or open addressing.
- Rehashing maintains performance as the table grows.
- Hash tables underpin many systems, from caches to databases and distributed services.


---

# Questions

1. What problem do hash tables solve?

> They provide fast lookup of values by key without searching every element.

2. Why are hash tables generally faster than linked lists for lookups?

> Because they use a hash function to jump directly to the expected bucket instead of traversing sequentially.

3. Why is a good hash function important?

> It distributes keys evenly, reducing collisions and maintaining near O(1) performance.

4. Why don't cryptographic hash functions make ideal hash table hash functions?

> They prioritize security over speed, while hash tables need fast, well-distributed hashing.

5. Why are hash tables widely used in caches?

> Because cached data must be retrieved by key with very low latency.

6. What happens if every key hashes to the same bucket?

> Performance degrades to O(n), similar to a linked list.

7. How do hash tables lead into concepts like consistent hashing?

> Both rely on hashing to map keys, but consistent hashing extends the idea to distribute keys across multiple machines while minimizing remapping when servers are added or removed.

8. What's the difference between a Hash Table and a Hash Map?
> A hash table is the underlying data structure that stores key-value pairs using hashing. A HashMap is a specific implementation of that data structure provided by a programming language or a standard library. Different languages implement their hash maps with different optimizations, resizing strategies, collision handling, and concurrency characteristics.





