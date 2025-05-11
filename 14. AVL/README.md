# 🧠 AVL Tree Insertion Explained (with Example)

AVL Tree is a **self-balancing Binary Search Tree** where the height difference (balance factor) between left and right subtrees is always at most 1.

During **insertion**, we:

1. Recursively insert the new node like in a normal BST.
2. Update the `height` of each node on the path back up.
3. Calculate the **balance factor** = `height(left) - height(right)`
4. **If unbalanced**, fix it using one of 4 **rotations** based on the direction of imbalance.

---

## 🔄 The 4 Rotation Cases

### 1. **LL (Left-Left)** – Right Rotation

> Grandchild is on **left of left** → Imbalance leans hard left

### 2. **RR (Right-Right)** – Left Rotation

> Grandchild is on **right of right** → Imbalance leans hard right

### 3. **LR (Left-Right)** – Left + Right Rotation

> Grandchild is on **right of left**

### 4. **RL (Right-Left)** – Right + Left Rotation

> Grandchild is on **left of right**

## 🧮 Recursive Insertion Logic

- Start from root and insert recursively.
- On return (bottom-up), update height.
- Then check balance and apply rotation **only if balance factor is not in [-1, 1]**.
- **Direction of grandchild decides the rotation.**
- **No need to memorize the code** — just draw and trace the nodes.

---

## 🌳 AVL Tree Insertion Example

Insert values in this order:

```text
30, 25, 35, 20, 15, 5, 10, 50, 60, 70, 65
```

Let’s walk through highlights:

### After inserting:

- `30, 25, 35, 20, 15, 5` → causes **LL** imbalance at 30
  👉 Right rotate at 30

### Then insert `10` under 5:

- causes **LR** at 20
  👉 Left rotate 5, right rotate 20

### Then insert `50, 60, 70`:

- causes **RR** at 35
  👉 Left rotate at 35

### Finally insert `65`:

- causes **RL** at 60
  👉 Right rotate at 70, left rotate at 60

---

✅ **Tip:** On each insert, trace back from the inserted node, check height and balance, and apply rotations if needed.

---

### ✍️ Practice this tree visually — the rotation logic becomes intuitive.
