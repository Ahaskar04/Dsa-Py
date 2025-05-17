# Sorting Algorithms: Classification by Space and Stability

Sorting is a fundamental concept in computer science, and sorting algorithms can be classified based on various properties. Two important dimensions are:

- **Space Usage**
- **Stability**

---

## 📦 1. Space Usage

Sorting algorithms can be classified as **In-Place** or **Out-of-Place** depending on how much extra memory they require.

### 🔁 In-Place Sorting

- Does **not** require extra space (or uses constant auxiliary space).
- Modifies the input array directly.
- Examples:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort (with in-place partitioning)
  - Heap Sort

### 📤 Out-of-Place Sorting

- Requires **additional space** proportional to the input size.
- Useful when original data must not be altered.
- Examples:
  - Merge Sort
  - Counting Sort
  - Radix Sort (in some implementations)
  - TimSort (uses temporary arrays)

---

## ⚖️ 2. Stability

Stability in sorting refers to preserving the **relative order** of records with equal keys.

### ✅ Stable Sorting

- Maintains the relative order of elements with equal keys.
- Important for multi-key sorting or sorting complex data.
- Examples:
  - Bubble Sort
  - Insertion Sort
  - Merge Sort
  - Counting Sort
  - TimSort

### ❌ Unstable Sorting

- May **reorder** equal elements.
- Faster in many cases, but not ideal when order matters.
- Examples:
  - Quick Sort
  - Heap Sort
  - Selection Sort

---

## 🧠 Summary Table

| Algorithm      | In-Place | Stable |
| -------------- | -------- | ------ |
| Bubble Sort    | ✅       | ✅     |
| Selection Sort | ✅       | ❌     |
| Insertion Sort | ✅       | ✅     |
| Merge Sort     | ❌       | ✅     |
| Quick Sort     | ✅       | ❌     |
| Heap Sort      | ✅       | ❌     |
| Counting Sort  | ❌       | ✅     |
| Radix Sort     | ❌       | ✅     |
| TimSort        | ❌       | ✅     |

---

## 📝 Notes

- **In-place algorithms** are memory-efficient but sometimes harder to implement.
- **Stable algorithms** are preferred when the original ordering of equal elements is significant.
