"""
hash_functions.py
 
Companion code for the "Hash Functions" chapter.
 
Demonstrates:
    - A simple custom hash function (for learning purposes only)
    - The deterministic property
    - Collisions
    - Distribution quality (good vs. poor)
    - A real-world cryptographic hash via hashlib
"""

import hashlib

# ---------------------------------------------------------------------------
# 1. A simple hash function (educational, NOT cryptographically secure)
# ---------------------------------------------------------------------------

def simple hash(key:str, table_size: int=1000) -> int:
  """
    Convert a string key into a fixed-size integer hash value.
 
    Uses a polynomial rolling hash:
        hash = (c0 * 31^(n-1) + c1 * 31^(n-2) + ... + cn) mod table_size
    """
   hash _value = 0
   for char in key:
     hash_value = (hash_value * 31 + ord(char)) % table_size
   return hash_value

# ---------------------------------------------------------------------------
# 2. Deterministic property
# ---------------------------------------------------------------------------

def deterministic():
  key = "Mutsa"
  print(f"Hash('{key}') -> {simple_hash(key)}")
  print(f"Hash('{key}') -> {simple_hash(key)}")  # same output every time

# ---------------------------------------------------------------------------
# 3. Collisions
# ---------------------------------------------------------------------------
def find_collision(words: list[str], table_size: int = 100):
    """
    Search a list of words for a hash collision at a given table size.
    Smaller table sizes make collisions more likely (good for demos).
    """
    seen = {}
    for word in words:
        h = simple_hash(word, table_size)
        if h in seen:
            print(f"Collision: '{seen[h]}' and '{word}' both hash to {h}")
        else:
            seen[h] = word


# ---------------------------------------------------------------------------
# 4. Distribution quality
# ---------------------------------------------------------------------------
def show_distribution(words: list[str], table_size: int = 100):
    """Print hash values to visually check how evenly they spread out."""
    for word in words:
        print(f"{word:>10} -> {simple_hash(word, table_size)}")
 
 
 
# ---------------------------------------------------------------------------
# 5. Real-world cryptographic hash (SHA-256)
# ---------------------------------------------------------------------------
def sha256_hash(text: str) -> str:
    """Return the SHA-256 hex digest of a string (e.g., for password storage)."""
    return hashlib.sha256(text.encode()).hexdigest()
 
 
if __name__ == "__main__":
    print("=== Deterministic ===")
    demo_deterministic()
 
    print("\n=== Distribution ===")
    sample_words = ["apple", "banana", "orange", "grape", "melon"]
    show_distribution(sample_words)
 
    print("\n=== Collisions (small table size) ===")
    find_collision(["Alice", "Bob", "Charlie", "David", "Eve", "Frank"], table_size=10)
 
    print("\n=== SHA-256 (real cryptographic hash) ===")
    print(f"sha256('hello') -> {sha256_hash('hello')}")  
