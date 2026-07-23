"""
AVL Tree — Simple Implementation
=================================
 

Operations implemented:
  insert(value)
  delete(value)
  search(value)   -> True/False
  height()
  inorder()     
"""

from __future__ import annotations

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 0 # height of a leaf node is 0


class AVLTree:
  def __init__(self):
    self.root = None

  #------------------------------------------------
  #Helpers
  #------------------------------------------------

  def _height)self, node) -> int:
    return node.height if node else -1

  def _balance_factor(self, node) -> int:
    return self._height(node.left) - self._height(node.right)

  def _update_height(self, node):
    node.height = 1 + max(self._height(node.left), self._height(node.right))


    # -----------------------------------------------------------------
    # Rotations
    # -----------------------------------------------------------------
  def _rotate_right(self, y):
        """
        Right rotation, used when the tree is left-heavy:
 
              y                    x
             / \\                  / \\
            x   T3   ---->      T1   y
           / \\                      / \\
          T1  T2                  T2  T3
        """
        x = y.left
        t2 = x.right
 
        x.right = y
        y.left = t2
 
        self._update_height(y)
        self._update_height(x)
      return x  # x is the new subtree root

    def _rotate_left(self, x):
        """
        Left rotation, used when the tree is right-heavy:
 
            x                       y
           / \\                     / \\
          T1  y      ---->        x   T3
             / \\                 / \\
            T2  T3              T1  T2
        """
        y = x.right
        t2 = y.left
 
        y.left = x
        x.right = t2
 
        self._update_height(x)
        self._update_height(y)
        return y  # y is the new subtree root
 
    def _rebalance(self, node):
        """Check balance factor and apply the correct rotation(s)."""
        self._update_height(node)
        balance = self._balance_factor(node)
 
        # Left-heavy
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)   # Left-Right case
            return self._rotate_right(node)                # Left-Left case
 
        # Right-heavy
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)  # Right-Left case
            return self._rotate_left(node)                   # Right-Right case
 
        return node  # already balanced
 
    # -----------------------------------------------------------------
    # Insert
    # -----------------------------------------------------------------
    def insert(self, value):
        self.root = self._insert(self.root, value)
 
    def _insert(self, node, value):
        if node is None:
            return Node(value)
 
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # duplicate, ignore
 
        return self._rebalance(node)
 
    # -----------------------------------------------------------------
    # Search
    # -----------------------------------------------------------------
    def search(self, value) -> bool:
        node = self.root
        while node:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False
 
    # -----------------------------------------------------------------
    # Delete
    # -----------------------------------------------------------------
    def delete(self, value):
        self.root = self._delete(self.root, value)
 
    def _delete(self, node, value):
        if node is None:
            return None
 
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Found the node to delete
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Two children: replace with in-order successor (smallest in right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
 
        return self._rebalance(node)
 
    # -----------------------------------------------------------------
    # Height / Traversal
    # -----------------------------------------------------------------
    def height(self) -> int:
        return self._height(self.root)
 
    def inorder(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result
 
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
 
 
# ---------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------
if __name__ == "__main__":
    avl = AVLTree()
 
    # Insert sorted data 1..7 — a plain BST would become a straight line
    # (height 6), but the AVL tree keeps rebalancing itself.
    values = [1, 2, 3, 4, 5, 6, 7]
    for v in values:
        avl.insert(v)
        print(f"inserted {v} -> height={avl.height()}, inorder={avl.inorder()}")
 
    print("\nFinal inorder (should be sorted):", avl.inorder())
    print("Final height (should be small, ~2, not 6):", avl.height())
 
    print("\nSearch 4:", avl.search(4))    # True
    print("Search 99:", avl.search(99))   # False
 
    avl.delete(1)
    avl.delete(2)
    print("\nAfter deleting 1 and 2:")
    print("inorder:", avl.inorder())
    print("height:", avl.height())
