"""
Queue Implementations — Hands-On Practice
==========================================
 
Three implementations of a Queue ADT:
  1. ArrayQueue      -> backed by a Python list (dynamic array)
  2. LinkedListQueue -> backed by a singly linked list (head=front, tail=rear)
  3. CircularQueue   -> backed by a fixed-size array with wrap-around indices

  Remember the application doesn't care how the queue is implemented; that's why we have an Array queue and a linked list queue.
 
Common interface (where it makes sense):
  enqueue(item)  -> add item to the rear
  dequeue()      -> remove & return the front item (raises on underflow)
  peek()         -> return the front item without removing it
  is_empty()     -> True/False
  size()         -> number of elements
 
Applications built on top:
  - PrinterQueue      -> simulate a FIFO print job queue
  - bfs(graph, start) -> Breadth-First Search using our own queue
"""

from __future__ import annotations # for type hints
from collections import deque as _deque #Python's built-in queue (we not gonna use it cause we are building a queue from scratch)

# Instead of just raising an Exception, we are going to create a meaningful one.

#---------------------------------------------------------------------
# Custom exceptions
#---------------------------------------------------------------------

class QueueUnderflowError(Exception):
  """Raised when dequeue() or peek() is called on an empty queue"""
  pass


class QueueOverflowError(Exception):
  """ Raised when enqueue() is called on a full fixed-capacity queue"""
  pass


# ---------------------------------------------------------------------------
# 1. Array-based Queue
# ---------------------------------------------------------------------------

class ArrayQueue:

  def __init__(self):
    self.data = []

  def enqueue(self, item):
    self.data.append(item)

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderflowError("dequeue from an empty ArrayQueue")
    return self.data.pop(0)

  def peek(self):
    if self.data.is_empty:
      raise QueueUnderflowError("peek on an empty ArrayQueue")
    return self.data[0]

  def is_empty(self):
    return len(self.data) == 0

  def size(self):
    return len(self.data)

  def __len__(self):
    return self.size()

  def __str__(self):
        return "Front -> " + " | ".join(repr(x) for x in self._data) + " <- Rear" \
            if self._data else "(empty)"


# ---------------------------------------------------------------------------
# 2. Linked-list-based Queue
# ---------------------------------------------------------------------------

class Node:
  __slots__ = ("value", "next")

  def __init__(self, value, next):
    self.value = value
     self.next = next
    

class LinkedListQueue:
    """ Queue implementation using a singly linked list.
 
    """
 
    def __init__(self):
        self._head = None   # front of queue
        self._tail = None   # rear of queue
        self._size = 0
 
    def enqueue(self, item):
        node = _Node(item)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1
 
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("dequeue from an empty LinkedListQueue")
        node = self._head
        self._head = node.next
        if self._head is None:      # queue became empty
            self._tail = None
        self._size -= 1
        return node.value
 
    def peek(self):
        if self.is_empty():
            raise QueueUnderflowError("peek on an empty LinkedListQueue")
        return self._head.value
 
    def is_empty(self):
        return self._head is None
 
    def size(self):
        return self._size
 
    def __len__(self):
        return self._size
 
    def __str__(self):
        items = []
        node = self._head
        while node:
            items.append(repr(node.value))
            node = node.next
        return "Front -> " + " | ".join(items) + " <- Rear" if items else "(empty)"



# ---------------------------------------------------------------------------
# 3. Circular Queue (fixed capacity, array-backed, O(1) enqueue/dequeue)
# ---------------------------------------------------------------------------

class CircularQueue:
    """Fixed-size queue using a circular (ring) buffer.
    """
 
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._size = 0
 
    def enqueue(self, item):
        if self.is_full():
            raise QueueOverflowError(
                f"CircularQueue is full (capacity={self._capacity})"
            )
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1
 
    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("dequeue from an empty CircularQueue")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
 
    def peek(self):
        if self.is_empty():
            raise QueueUnderflowError("peek on an empty CircularQueue")
        return self._data[self._front]
 
    def is_empty(self):
        return self._size == 0
 
    def is_full(self):
        return self._size == self._capacity
 
    def size(self):
        return self._size
 
    def __len__(self):
        return self._size
 
    def __str__(self):
        if self.is_empty():
            return "(empty)"
        items = [self._data[(self._front + i) % self._capacity] for i in range(self._size)]
        return "Front -> " + " | ".join(repr(x) for x in items) + " <- Rear"

# ---------------------------------------------------------------------------
# Application 1: Printer Queue Simulation
# ---------------------------------------------------------------------------

class PrintJob:
    def __init__(self, doc_name: str, pages: int):
        self.doc_name = doc_name
        self.pages = pages
 
    def __repr__(self):
        return f"{self.doc_name} ({self.pages}pg)"
 
 
class PrinterQueue:
    """A FIFO printer queue: jobs are printed in the order submitted.
 
    Uses our own LinkedListQueue internally — swap in ArrayQueue or
    CircularQueue and it behaves identically.
    """
 
    def __init__(self, pages_per_minute: int = 10, queue_cls=LinkedListQueue):
        self._queue = queue_cls()
        self._pages_per_minute = pages_per_minute
 
    def submit_job(self, doc_name: str, pages: int):
        job = PrintJob(doc_name, pages)
        self._queue.enqueue(job)
        print(f"[submitted] {job}")
 
    def is_idle(self):
        return self._queue.is_empty()
 
    def process_all(self):
        """Process every job currently in the queue, FIFO order."""
        total_minutes = 0.0
        while not self._queue.is_empty():
            job = self._queue.dequeue()
            minutes = job.pages / self._pages_per_minute
            total_minutes += minutes
            print(f"[printing] {job} -> {minutes:.1f} min")
        print(f"[done] total time: {total_minutes:.1f} min")
        return total_minutes
 
 
  # ---------------------------------------------------------------------------
# Application 2: Breadth-First Search (BFS) using our own queue
# ---------------------------------------------------------------------------
def bfs(graph: dict, start, queue_cls=LinkedListQueue):
    """
    Standard BFS traversal of a graph given as an adjacency list, e.g.:
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C'],
        }
 
    Returns the list of nodes in the order they were visited.
 
    Uses our queue to hold the "frontier" of nodes to explore next —
    the defining trait of BFS vs. DFS (which would use a stack instead).
    """
    visited = {start}
    order = []
    q = queue_cls()
    q.enqueue(start)
 
    while not q.is_empty():
        node = q.dequeue()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.enqueue(neighbor)
 
    return order
 
 
# ---------------------------------------------------------------------------
# Demo 
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Basic Queue Operations ===")
    for make_queue in (lambda: ArrayQueue(),
                       lambda: LinkedListQueue(),
                       lambda: CircularQueue(5)):
        q = make_queue()
        print(f"\n-- {type(q).__name__} --")
        print("is_empty:", q.is_empty())
 
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        print("after enqueues:", q)
        print("peek (front):", q.peek())
        print("dequeue:", q.dequeue())
        print("after dequeue:", q)
        print("size:", q.size())

        # Drain and trigger underflow
        while not q.is_empty():
            q.dequeue()
        try:
            q.dequeue()
        except QueueUnderflowError as e:
            print("Caught underflow:", e)
 
    print("\n-- CircularQueue overflow check --")
    cq = CircularQueue(3)
    cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
    print("full?", cq.is_full())
    try:
        cq.enqueue(4)
    except QueueOverflowError as e:
        print("Caught overflow:", e)
    # Demonstrate wrap-around: dequeue then enqueue reuses freed slot
    cq.dequeue()
    cq.enqueue(4)
    print("after wrap-around enqueue:", cq)
 
    print("\n=== Printer Queue Simulation ===")
    printer = PrinterQueue(pages_per_minute=20)
    printer.submit_job("resume.pdf", 2)
    printer.submit_job("thesis.docx", 150)
    printer.submit_job("invoice.pdf", 1)
    printer.process_all()

    print("\n=== Breadth-First Search ===")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }
    order = bfs(graph, 'A')
    print("BFS order from 'A':", order)
    # Cross-check with all three queue backends give the same traversal order
    for Q in (ArrayQueue, LinkedListQueue):
        assert bfs(graph, 'A', queue_cls=Q) == order
    print("BFS order matches across ArrayQueue and LinkedListQueue ✔")
 
