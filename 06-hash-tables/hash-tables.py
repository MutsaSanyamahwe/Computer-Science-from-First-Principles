"""
hash_tables.py
 
Companion code for the "Hash Tables" chapter.
 
Builds on hash_functions.py. Implements a hash table from scratch using
the two classic collision resolution strategies:
 
    1. Separate Chaining  - each slot holds a list (bucket) of entries
    2. Open Addressing    - on collision, probe for the next free slot
 
Both support: insert, get, delete, and resizing.
"""

from hash_functions import simple_hash

# ---------------------------------------------------------------------------
# 1. Separate Chaining
# ---------------------------------------------------------------------------

class ChainingHashTable:
    """
    Each bucket is a list of (key, value) pairs. On collision, the new
    pair is simply appended to the same bucket's list.
    """


    def __init__(self, capacity: int = 0):
      self.capacity = capacity
      self.size = 0
      self.buckets: list[list[tuple]] = [[] for _ in range(capacity)]

    def _index(self, key:str) -> int:
      return simple_hash(key. self.capacity) #checkout the simple_hash function in hash-functions.py

    def put(self, key:str, value) -> None:
      index = self._index(key)
      bucket = self.buckets[index]

      for i, (k, _) in enumerate(bucket):
        if k == key:
          bucket[i] = (key, value) # update existing key
          return

      bucket.append(key,value))
      self.size += 1

      if self.size / self.capacity > 0.75: # load factor threshold
          self.resize()

    def get(self, key: str):
        index = self._index(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        raise KeyError(key)
 
    def delete(self, key: str) -> None:
        index = self._index(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)
 
    def _resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
 
    def __contains__(self, key: str) -> bool:
        index = self._index(key)
        return any(k == key for k, _ in self.buckets[index])
 
    def __repr__(self) -> str:
        items = [f"{k!r}: {v!r}" for bucket in self.buckets for k, v in bucket]
        return "{" + ", ".join(items) + "}"
    
  
# ---------------------------------------------------------------------------
# 2. Open Addressing (linear probing)
# ---------------------------------------------------------------------------

_DELETED = object()  # sentinel to mark deleted slots without breaking probes
 
 
class OpenAddressingHashTable:
    """
    A single flat array of slots. On collision, probe forward
    (linear probing) until an empty slot is found.
    """
 
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.keys: list = [None] * capacity
        self.values: list = [None] * capacity
 
    def _index(self, key: str) -> int:
        return simple_hash(key, self.capacity)
 
    def put(self, key: str, value) -> None:
        if self.size / self.capacity > 0.7:
            self._resize()
 
        index = self._index(key)
        first_deleted = None
 
        for _ in range(self.capacity):
            slot = self.keys[index]
            if slot is None:
                target = first_deleted if first_deleted is not None else index
                self.keys[target] = key
                self.values[target] = value
                self.size += 1
                return
            if slot is _DELETED and first_deleted is None:
                first_deleted = index
            elif slot == key:
                self.values[index] = value  # update existing key
                return
            index = (index + 1) % self.capacity
 
        raise RuntimeError("Hash table is full")  # shouldn't happen due to resizing
 
    def get(self, key: str):
        index = self._index(key)
        for _ in range(self.capacity):
            slot = self.keys[index]
            if slot is None:
                break
            if slot == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        raise KeyError(key)
 
    def delete(self, key: str) -> None:
        index = self._index(key)
        for _ in range(self.capacity):
            slot = self.keys[index]
            if slot is None:
                break
            if slot == key:
                self.keys[index] = _DELETED
                self.values[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity
        raise KeyError(key)
 
    def _resize(self) -> None:
        old_keys, old_values = self.keys, self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        for k, v in zip(old_keys, old_values):
            if k is not None and k is not _DELETED:
                self.put(k, v)
 
    def __contains__(self, key: str) -> bool:
        try:
            self.get(key)
            return True
        except KeyError:
            return False
 
    def __repr__(self) -> str:
        items = [
            f"{k!r}: {v!r}"
            for k, v in zip(self.keys, self.values)
            if k is not None and k is not _DELETED
        ]
        return "{" + ", ".join(items) + "}"




if __name__ == "__main__":
    print("=== Separate Chaining ===")
    chain_table = ChainingHashTable(capacity=4)
    chain_table.put("Alice", 30)
    chain_table.put("Bob", 25)
    chain_table.put("Charlie", 35)  # will likely collide at capacity=4
    print(chain_table)
    print(f"Bob -> {chain_table.get('Bob')}")
    chain_table.delete("Bob")
    print(f"'Bob' in table? {'Bob' in chain_table}")
    print(chain_table)
 
    print("\n=== Open Addressing (linear probing) ===")
    open_table = OpenAddressingHashTable(capacity=4)
    open_table.put("Alice", 30)
    open_table.put("Bob", 25)
    open_table.put("Charlie", 35)
    print(open_table)
    print(f"Charlie -> {open_table.get('Charlie')}")
    open_table.delete("Alice")
    print(f"'Alice' in table? {'Alice' in open_table}")
    print(open_table)
 
    print("\n=== Resizing in action ===")
    growing_table = ChainingHashTable(capacity=2)
    for name in ["Alice", "Bob", "Charlie", "David", "Eve"]:
        growing_table.put(name, True)
        print(f"After inserting {name}: capacity={growing_table.capacity}, size={growing_table.size}")

  
