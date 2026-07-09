# Queues

## 1. The Problem

Imagine customers arriving at a supermarket checkout.

The first customer to arrive should be the first customer served.

If a customer who just arrived could go to the front of the line, the system would be unfair and unpredictable.

Many computer systems have the same requirement:
- print jobs
- Customer support tickets
- Incoming web requests
- Message processing
- Task scheduling

We need a way to process items in the exact order they arrive.

---

## 2. The Solution

A queue is a linear data structure that follows the First In, First Out (FIFO) principle.

The first element added is the first one removed.

Imagine people standing in line.

```
Front                    Rear
x x x x  
```

New people join at the rear.

People leave from the front.

---

## 3. Core Operations

**Enqueue**
Adds an item to the rear (back of the queue)

Before

```
Front         Rear

A → B → C
```

Enqueue D

After
```
Front             Rear

A → B → C → D
```
Time complexity

```
O(1)
```
----

**Front (Peek)**
Returns the front item without removing it.

```
Front

A → B → C
```

Returns 

```
A
```
Time Complexity

```
O(1)
```

---

**Is Empty**
Checks whether the queue contains any elements.

Time Complexity
```
O(1)
```

---

## 4. How a Queue Works

A queue keeps track of two positions:

```
Front

Rear

```
When data arrives:
- Add it to the rear.

When data is processed:
- Remove it from the front.

Example:

```
Enqueue A

A

Enqueue B

A B

Enqueue C

A B C

Dequeue

B C

Dequeue

C
```

Notice that the oldest item always leaves first.

---

## 5. Implementing a Queue

A queue is an Abstract Data Type (ADT)
It defines behavior rather than implementation.

**Using an Array**

```
Front            Rear

0   1   2   3

A   B   C
```

Advatanges
- Excellent cache locality
- Simple implementation

Disadvantages
- A basic array implementation may require shifting elements after each dequeue
- A circular queue avoids this problem

---


**Using a linked List**

```
Front                 Rear

A → B → C → D
```

Advatanges
- Dynamic size
- No shifting required
- O(10 enqueue and dequeue when maintaining both front and rear pointers

Disadvatages
- Extra memory for pointers
- Poor cache locality

---

## 6. Circular Queue

Instead of moving every element after dequeue, the queue wraps around to the beginning of the array.

```
+---------------------+

A  B  C  _  _

+---------------------+

Front
```

After several operations:

```
+---------------------+

_  _  C  D  E

+---------------------+

      ↑
Front
```

When the rear reaches the end, it continues at the beginning.

This avoids unnecessary copying.

---

## 7. Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Enqueue   | O(1)       |
| Dequeue   | O(1)       |
| Peek      | O(1)       |
| Is Empty  | O(1)       |
| Search    | O(n)       |


---

## 8. Advatages

- Fair processing order
- Fast insertion and removal
- Simple implementation
- Widely used in scheduling systems

---

## 9. Disadvantages
- No random access
- Searching is O(n)
- Only the front element is immediately accessible

---

## 10. Types of Queues

### Linear Queue
Standard FIFO queue

```
Front

A → B → C

          Rear
```

---

### Circular Queue
The rear wraps back to the beginning of the array.

Useful for fixed-size buffers

---

### Priority Queue
Elements are processed according to priority rather than arrival time.

```
High Priority

↓

Medium

↓

Low
```

Example:
Emergency room patients.

Highest priority is treated first.

---

### Double-Ended Queue (Deque)
Insertion and removal can happen at both ends.

```
← A ↔ B ↔ C →
```

Useful for sliding window algorithms and task scheduling.

---

## 11. Real-World Uses

Printer Queue
Print jobs are processed in arrival order

```
Job1

↓

Job2

↓

Job3
```

---
Messaging Queues

Systems like RabbitMQ. Kafka (at the partition level), and cloud messaging services use queues to decouple producers from consumers.

```
Producer

↓

Queue

↓

Consumer
```

---

Web Servers

Incoming HTTP requests are often queued before being handled by worker threads.

---

CPU Scheduling
Operating systems maintain queues for processing tasks waiting to execute.

---

Breadth-First Search (BFS)
BFS explores nodes level by level using a queue.

```
A

↓

B   C

↓

D E F G

```

---

## 12. Why System Designers Care
Queues are one of the most important concepts in distributed systems.

They help:
- Buffer traffic spikes
- Decouple producers from consumers
- Smooth out workload between services
- Enable asynchronous processing
- Improve system reliability by preventing request loss during bursts.

Examples include:
- Order processing in e-commerce
- Background email sending
- Image and video delivery
- Job scheduling systems

Understanding queues is essential before learning about message brokers and event-driven architectures.

---

## 13. Key Takeaways
- Queues follow the First In, First Out (FIFO) principle.
- Elements are added at the rear and removed from the front
- Enqueue and dequeue are O(1)
- Queues can be implemented using arrays or linked lists.
- Circular queues eliminate unnecessary shifting
- Queues are fundamental to scheduling, networking, and distributed systems

---

## Questions
1. What problem does a circular queue solve?
> It reuses freed array space, avoiding expensive element shifting.

2. When would you implement a queue using a linked list?
> When you need a dynamically sized queue with O(1) enqueue and dequeue.

3. Why are queues essential in distributed systems?
> They decouple components, absorb traffic spikes, and allow asynchronous processing.

4. Why does Breadth-First Search (BFS) require a queue?
> BFS processes nodes level by level in the order they are discovered, which matches FIFO behavior.

5. Why might a web server queue incoming requests?
> To manage bursts of traffic and distribute work among available workers.

6. When should you use a priority queue instead of a standard queue?
> When processing order should depend on importance rather than arrival time.

7. Why are message queues important in microservices?
> They enable services to communicate asynchronously, improving scalability, resilience, and fault isolation.

---


