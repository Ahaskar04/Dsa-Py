# Hashing Collision Resolution Techniques

When multiple keys hash to the same index in a hash table (a collision), we need strategies to handle them. Below are two primary methods for collision resolution:

## 1. Direct Chaining

- This method uses a linked list at each index of the hash table.
- If multiple elements hash to the same index, they are stored in the linked list at that index.
- **Best suited when deletions are frequent**, as removing nodes from a linked list is straightforward and efficient.

## 2. Open Addressing

- Instead of using linked lists, all elements are stored within the hash table itself.
- When a collision occurs, the algorithm searches for the next available slot based on a probing technique.
- **Best used when the size of the array (hash table) is known in advance**, as it requires a fixed-size array and performs better with less dynamic resizing.

### \* Linear Probing

- Checks the next slot sequentially until an empty one is found.
- May lead to clustering (grouping of filled slots).

### \* Quadratic Probing

- Uses a quadratic function (e.g., 1², 2², 3², ...) to find the next slot.
- Reduces clustering compared to linear probing.

### \* Double Hashing

- Uses a second hash function to calculate the step size for probing.
- Offers better distribution and minimizes clustering.

These are foundational techniques used in designing efficient hash tables.
