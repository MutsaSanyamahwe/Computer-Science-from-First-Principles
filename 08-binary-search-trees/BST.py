"""
Binary Search Tree (BST) 
=================================================
 
Operations implemented:
  insert(value)
  search(value)   -> True/False
  delete(value)
  min_value() / max_value()
  height()
  inorder() / preorder() / postorder()  -> traversals as lists
"""


from __future__ import annotations

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  #--------------------------------------------------
  # insert
  #--------------------------------------------------

  def insert(self,value):
    self.root = self._insert(self.root, value)

  def _insert(self, node, value):
    if node is None:
      return Node(value)
    if value < node.value:
      node.left = self.insert(node.left, value)
    elif value > node.value:
      node.right = self.insert(node.right, value)
    #else: value already exists, ignore duplicates
    return node


  #--------------------------------------------------
  # Search
  #--------------------------------------------------

  def search(self, value) -> bool:
    return self.search(self.root, value)

  def _search(self, node, value) -> bool:
    if node is None:
      return False
    if value == node.value:
      return True
    return self.search(node.left, value) if value , node.value \
      else self._search(node.right, value)

    # -----------------------------------------------------------------
    # Min / Max
    # -----------------------------------------------------------------
    def min_value(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        node = self.root
        while node.left:
            node = node.left
        return node.value
 
    def max_value(self):
        if self.root is None:
            raise ValueError("Tree is empty")
        node = self.root
        while node.right:
            node = node.right
        return node.value
      
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
            # Two children: replace value with the smallest value in the
            # right subtree (in-order successor), then delete that node.
            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
 
        return node

    # -----------------------------------------------------------------
    # Height
    # -----------------------------------------------------------------
    def height(self) -> int:
        return self._height(self.root)
 
    def _height(self, node) -> int:
        if node is None:
            return -1  # empty tree has height -1, single node has height 0
        return 1 + max(self._height(node.left), self._height(node.right))
 
    # -----------------------------------------------------------------
    # Traversals
    # -----------------------------------------------------------------
    def inorder(self) -> list:
        """Left -> Node -> Right. Produces values in sorted order."""
        result = []
        self._inorder(self.root, result)
        return result
 
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
 
    def preorder(self) -> list:
        """Node -> Left -> Right. Useful for copying/serializing a tree."""
        result = []
        self._preorder(self.root, result)
        return result
 
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
 
    def postorder(self) -> list:
        """Left -> Right -> Node. Useful for deleting a tree bottom-up."""
        result = []
        self._postorder(self.root, result)
        return result
 
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
 
 
# ---------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------
if __name__ == "__main__":
    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)
 
    print("Inorder (sorted):", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]
    print("Preorder:", bst.preorder())             # [50, 30, 20, 40, 70, 60, 80]
    print("Postorder:", bst.postorder())           # [20, 40, 30, 60, 80, 70, 50]
 
    print("Search 40:", bst.search(40))            # True
    print("Search 100:", bst.search(100))          # False
 
    print("Min:", bst.min_value())                 # 20
    print("Max:", bst.max_value())                 # 80
    print("Height:", bst.height())                 # 2
 
    bst.delete(30)  # node with two children
    print("Inorder after deleting 30:", bst.inorder())  # [20, 40, 50, 60, 70, 80]
 
