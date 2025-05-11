# 🗑️ AVL Tree Deletion Explained

Deletion in an AVL Tree is similar to deletion in a Binary Search Tree, but after deleting a node, we must ensure the tree remains balanced.

---

## 🔹 Case 1: No Rotation Needed

These are standard BST deletions — AVL tree behaves normally here.

### 1. Leaf Node

- Node to delete has no children.
- Simply remove it.

### 2. One Child

- Replace the node with its child directly.

### 3. Two Children

- Find **inorder successor** (smallest value in right subtree).
- Replace the node’s value with successor’s.
- Recursively delete the successor node.

After any of these, **update heights** and check balance factors on the way back up.

---

## 🔁 Case 2: Rotation Needed

After deletion, a node might become **unbalanced**.
We check balance factor at each ancestor node and apply rotations:

### Same 4 Classic Cases:

1. **LL (Left-Left)** ➝ `Right Rotate`
2. **RR (Right-Right)** ➝ `Left Rotate`
3. **LR (Left-Right)** ➝ `Left + Right Rotate`
4. **RL (Right-Left)** ➝ `Right + Left Rotate`

---

## 🔄 Notes

- Balance factor = `height(left) - height(right)`
- Recalculate height and balance **on the way back up (bottom-up recursion)**.
- **Rotation logic is identical to insertion.**
- Deletion may cause multiple unbalanced nodes, so fix all along the path.

---

✅ **Tip:** Don’t memorize rotations — draw the tree and follow balance factors.
