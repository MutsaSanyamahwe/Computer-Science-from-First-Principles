# Tries

## 1. The Problem

So far, we've mostly studied data structures that organize data around values.

For example, a Binary Search Tree organizes numbers:

```
                50
              /    \
            30      70
```

A B-Tree and B+ Tree extend this idea to large datasets and storage systems.

But consider a different type of data.

Suppose we have a dictionary containing:

```
cat
car
can
care
card
dog
```

Now imagine we want to answer questions like:

- Does the word `car` exist?
- What words begin with `ca`?
- What words begin with `car`?
- Give me all possible completions for `ca`.

A hash table can tell us whether:

```
"car"

```

exists.

But it doesn't naturally organize the words according to their prefixes.

A sorted array can help with prefixes, but finding and managing prefixes becomes more complicated.

We need structure where:

> The structure itself represents the characters that words have in commmon.

This leads to the Trie.

---

## 2. The Solution

A Trie is a tree-like data structure designed to store and retrieve strings based on their individual characters.

Instead of treating:

```
"car"
```

as one complete value, a Trie breaks it into:

```
c → a → r
```

For example:

```
        root
         |
         c
         |
         a
        / \
       r   n
       |   |
       e   ...
```

Words that share the same prefix share the same path through the tree.

For example:

```
cat
car
can
```

all begin with:

```
c → a
```

So the Trie stores that shared structure only once.

---

## 3. The Core Idea

The most important idea behind a Trie is:

> Each edge represents a character, and each path represents a string.

Consider:

```
cat
car
can

```


The Trie becomes:

```
             root
               |
               c
               |
               a
            /  |  \
           t   r   n
```

The path:

```
root → c → a → t
```

and so on.

---

## 4. But How Do We Know Where a Word Ends?

Consider:

```
car
care

```

Their paths overlap:

```
c → a → r → e
```
How do we distinguish car from the prefix of care?

Trie nodes therefore usually contain an indicator such as:

```
is_end_of_word
```

For example:

```
        root
         |
         c
         |
         a
         |
         r  ← is_end_of_word = True
         |
         e  ← is_end_of_word = True
```

This means:

```
car   ✓
care  ✓
```

The `r` node marks the end of one complete word, while the `e` marks the end of another.

---

## 5. Shared Prefixes

This is the fundamental advantage of a Trie.

Suppose we insert:

```
apple
application
apply
```

All three begin with:

```
a → p → p → l

```
The Trie shares that path:

```
                 root
                   |
                   a
                   |
                   p
                   |
                   p
                   |
                   l
                 /   \
                e     y
                |
                ...
```

Instead of treating every word independently, the Trie represents their common structure.

This makes prefix operations particularly natural.

---

## 6. Insertions

To insert a word:

```
"cat"
```

we process one character at a time.

> Step 1

Start at the root.

```
root

```

> Step 2

Look for:

```
c
```

If it doesn't exist, create it.

```
root
  |
  c

```

> Step 3

Process:

```
a
```

```
root
  |
  c
  |
  a
```

> Step 4

Process:

```

t

```

```
root
  |
  c
  |
  a
  |
  t
```

> Step 5

Mark the final node:

```
is_end_of_word = True
```

The Trie now represents:

```
cat
```

---

## 8. Searching

Suppose the Trie contains:

```
cat
car
can
```

We want to search for:

```
car
```

Start at the root.

> Character 1

Find:

```
c
```

> Character 2

Find:

```
a
```

> Character 3

Find:

```

r

```

Now check:

```
is_end_of_word

```

If it is `True`:

```
car ✓
```

The search follows one character at a time.

---

## 9. Searchinh for a Prefix

This is where Tries become especially powerful.

Suppose we search for:

```
"ca"

```

We follow:

```
root → c → a
```
We have successfully reached the prefix.

From that node we can explore everything underneath it:

```
          c
          |
          a
        / | \
       t  r  n

```

Therefore:

```
ca
├── cat
├── car
└── can

```

This makes prefix searching extremely natural.

---

## 10. Autocomplete

This leads directly to one of the most recognizable applications of a Trie.

Suppose you're typing into a search box:

```
ca

```


The system might suggest:

```
cat
car
card
care
camera
```

The Trie can:

1. Follow `c`
2. Follow `a`
3. Find the node representing `ca`
4. Traverse the subtree beneath it
5. Collect possible words

Conceptually:

```
                    ca
                  /    \
                 t      r
                       / \
                      d   e

```

The system can discover all words sharing the prefix.

---

## 11. Prefix Search vs Hash Tables

This is an important comparison.

Suppose we have a hash table:

```
{
    "cat",
    "car",
    "can",
    "dog"
}

```

A hash table is excellent for:

```
Does "car" exist?
```

But asking:

```
What words begin with "ca"?
```

is not its natural operation.

You may have to inspect many stored keys.

A Trie directly represents the prefix:

```
root
 |
 c
 |
 a
```

Everything below that node shares the prefix.

So:

> Hash tables optimize exact-key lookup. Tries optimize string and prefix-based lookup.


---

## 12. Complexity

Let `L` be the length of the string.

> Insertion

```
O(L)
```

> Search

```
O(L)
```

> Prefix search

Finding the prefix takes:

```
O(L)
```


After that, collecting `k` matching words requires additional work depending on the size of the matching subtree.

So conceptually:

```
O(L + k)
```

where `k` represents the amount of matching output that must be traversed/returned.

The important point is that these operations depend primarily on the length of the word, rather than directly on the total number of stored words.


---

## 13. The Cost of Tries

Tries have an important trade-off.

They can consume a lot of memory.

Consider an alphabet with 26 possible lowercase characters.

A simple Trie node might conceptually contain:

```
children[26]

```


Even if only one character is actually used from that node, space may be reserved for many possible children.

For example:

```
        [a,b,c,d,e,...,z]
```

This can become expensive for very large datasets.

Therefore, implementations may use different representations for children, such as:

```
Array
Dictionary / Hash Map
Map
Compressed representation
```

There is a trade-off between:

```
Speed
   ↕
Memory
```

---

## 14. Trie vs Binary Search Tree

| **BST**                                 | **Trie**                                 |
| --------------------------------------- | ---------------------------------------- |
| Organizes values using comparisons      | Organizes strings character-by-character |
| Nodes contain complete values           | Paths represent strings                  |
| Based on ordering                       | Based on prefixes                        |
| Search depends on tree height           | Search depends on string length          |
| Good for ordered values                 | Excellent for prefix operations          |
| Can store many types of comparable data | Primarily designed for strings/sequences |


The key difference is:

> A BST asks "Is this value smaller or larger?" A Trie asks "What character comes next?"


---

## 15. Trie vs Hash Table

| **Hash Table**                      | **Trie**                            |
| ----------------------------------- | ----------------------------------- |
| Excellent exact lookup              | Excellent string lookup             |
| Average O(1) exact lookup           | O(L) lookup                         |
| Doesn't naturally preserve prefixes | Naturally represents prefixes       |
| No inherent ordering                | Can represent lexicographical order |
| Often memory efficient              | Can consume significant memory      |
| Good for key-value lookup           | Good for autocomplete/prefix search |

 
Neither structure is universally better.

They solve different problems.

---

## 16 Advantages

- Fast string insertion.
- Fast string lookup.
- Efficient prefix searches.
- Natural support for autocomplete.
- Shared prefixes reduce duplicated structural information.
- Can produce lexicographically ordered results.
- Performance depends primarily on string length.

---

## 17. Disadvantages

- Can consume significant memory.
- More complicated than a hash table for simple key-value lookup.
- Large alphabets can increase memory requirements.
- Many nodes may contain only a small amount of useful information.
- Requires specialized implementations to optimize memory usage.

---

## 18. Real-World Applications

Tries are useful when systems need to work with strings and prefixes.

Examples include:


> Autocomplete

```
ca
 ↓
car
card
care
cat
camera

```

> Search suggestions

Search engines can use prefix structures to find possible completions.

> Spell checking

A Trie can represent a dictionary of valid words.

```
hello
help
helicopter
```

> IP routing

Trie-like structures can represent prefixes such as:

```
192.168...
```

or binary prefixes used in network routing.

> Dictionary systems

A Trie can efficiently determine whether a sequence forms a valid word.


---

## 19. The Big Picture

Your tree progression now becomes:

```
Binary Tree
      ↓
Binary Search Tree
      ↓
Need guaranteed balance
      ↓
AVL Tree
      ↓
Red-Black Tree
      ↓
Need to handle large persistent datasets
      ↓
B-Tree
      ↓
Need efficient range scanning
      ↓
B+ Tree
      ↓
Now consider a different problem:
      ↓
We need to organize STRINGS
      ↓
Especially shared prefixes
      ↓
Trie
```


The important shift is that a Trie isn't primarily concerned with:

> "Which value is larger?"

Instead, it is concerned with:

> "Which character comes next?"


---

# Questions

1. What problem does a Trie solve?

> It efficiently stores and retrieves strings, particularly when operations involve prefixes.

2. What does each edge in a Trie represent?

> Usually one character.

3. What does a path from the root represent?

> A string or prefix.

4. Why do Tries need an end-of-word marker?

> Because one word can be a prefix of another word, so we need to distinguish a complete word from merely a prefix.

5. Why are Tries useful for autocomplete?

> Because all words sharing a prefix are located in the subtree beneath that prefix's node.

6. What is the search complexity?

> O(L), where L is the length of the string.

7. What is the biggest disadvantage of a Trie?

> Memory consumption can be high because the structure may contain many nodes and child references.

8. How is a Trie different from a BST?

> A BST organizes values through comparisons, while a Trie organizes strings character-by-character.

9. How is a Trie different from a hash table?

> A hash table is optimized for exact key lookup, while a Trie naturally supports prefix-based operations.

10. What is the key idea behind a Trie?

> Shared prefixes share paths.

11. Why is "car" different from the prefix "car" in "care"?

> The Trie uses an end-of-word marker to indicate whether the current node represents a complete stored word.

12. What problem is a Trie fundamentally solving?

> Efficient retrieval and organization of strings based on their characters and shared prefixes.
