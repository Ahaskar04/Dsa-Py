# Binary Heap in Python

A binary heap is a **complete binary tree** that satisfies the heap property — useful in many algorithms such as **Heap Sort**, **Priority Queues**, and **graph algorithms like Prim's Algorithm**.

## 1. Types of Binary Heap

There are two main types of binary heaps:

- **Min Heap**: In a Min Heap, the parent node is always less than or equal to its children. The smallest element is always at the root.
- **Max Heap**: In a Max Heap, the parent node is always greater than or equal to its children. The largest element is always at the root.

This implementation supports both Min and Max heaps, specified by the user during insertion or extraction.

## 2. Core Algorithms Using Binary Heap

The binary heap plays a critical role in the following algorithms:

- **Prim’s Algorithm**: Used to find the Minimum Spanning Tree (MST) of a graph. A priority queue (min-heap) is used to efficiently retrieve the next minimum-weight edge.
- **Heap Sort**: A comparison-based sorting algorithm that builds a heap from the input data and then extracts the maximum (or minimum) one by one.
- **Priority Queue**: A data structure where elements are retrieved according to their priority. Heaps are commonly used to implement priority queues for fast insert and extract operations.
