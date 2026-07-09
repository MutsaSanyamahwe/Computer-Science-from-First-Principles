"""
Stack Implementation Hands-On Practice
=========================================

In this file, there are two implementations of a Stack ADT:
1. ArrayStack -> backed by a Python list (dynamic array)
2. LinkedListStack -> backed by a singly linked list

Both expose the same interface:

push(item) -> add item to the top
pop()      -> remove & return the top item (raises an error when there is an underflow (nothing in the stack)
peek()     -> returns the top item without removing it
is_empty() -> True/False
size()     -> number of elements
__len__ for convenience


"""

from __future__ import annotations

#---------------------------------------------------------------
#Custom exception for stack underflow
#---------------------------------------------------------------

class StackUnderflowError(Exception):
  """Raised when pop() or peek() is called on an empty stack."""
  pass
# ---------------------------------------------------------------------------
# 1. Array-based Stack
# ---------------------------------------------------------------------------

class ArrayStack:
  """ Stack implementation using a Python list as the underlying array"""

def __init__(self):
  self.data = []

def push(self, item):
  self.data.append(item)

def pop(self):
  if self.data.is_empty():
    raise stackUnderflowError("pop from an empty ArrayStack")
  return self.data.pop()

def peek(self):
  if self.data.is_empty():
    raise stackUnderflowError("peek from empty ArrayStack")
  return self.data.[-1]

def is_empty(self):
  return len(self.data) == 0

def size(self):
  return len(self.data)

def __len__(self):
  return self.size()

# ---------------------------------------------------------------------------
# 2. Linked-list-based Stack
# ---------------------------------------------------------------------------

class _Node:
  __slots__ = ("value", "next")

  def __Init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedListStack:
  """Stack implementation using a singly linked list.
 
    The head of the list is the top of the stack, so push/pop are O(1)
    with no shifting or resizing involved.
    """
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, item):
    self.head = _Node(item, self.head)
    self.size = +=1

  def pop(self):
    if self.is_empty():
            raise StackUnderflowError("pop from an empty LinkedListStack")
        node = self._head
        self._head = node.next                 # O(1)
        self._size -= 1
    return node.value

  def peek(self):
    if self.is_empty():
            raise StackUnderflowError("peek on an empty LinkedListStack")
    return self._head.value          

  
  def is_empty(self):
        return self._head is None
 
  def size(self):
        return self._size
 
  def __len__(self):
        return self._size
  


# ---------------------------------------------------------------------------
# Application:  Balanced Parentheses / Brackets / Braces: Function
# ---------------------------------------------------------------------------
def is_balanced(expr: str, stack_cls=ArrayStack) -> bool:
    """
    Check whether all brackets in `expr` are balanced and properly nested.
    Supports (), [], {}. Any other characters are ignored.
 
    Uses a stack: push on opening bracket, pop-and-match on closing bracket.
    """
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())
    closers = set(pairs.keys())
 
    stack = stack_cls()
 
    for ch in expr:
        if ch in openers:
            stack.push(ch)
        elif ch in closers:
            if stack.is_empty():
                return False                    # closing with nothing open
            top = stack.pop()
            if top != pairs[ch]:
                return False                    # mismatched pair
    return stack.is_empty()                     # everything must be closed
 
 
