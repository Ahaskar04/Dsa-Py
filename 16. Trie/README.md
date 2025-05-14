# Understanding the Trie Structure for Word Insertion

### ❌ Incorrect Trie Assumption:

```python
cur = {c: TrieNode, a: TrieNode, t: TrieNode}
```

This structure is **incorrect** because it implies that all characters `c`, `a`, and `t` are direct children of the root node. In a Trie, **each character** in the word occupies **a different level** in the tree.

---

### ✅ Correct Trie Structure for the Word `"cat"`:

Each `TrieNode` contains:

- `children`: a dictionary mapping characters to child `TrieNode`s
- `endOfWord`: a boolean indicating whether the current node marks the end of a valid word

```python
cur = {
  'c': TrieNode(
         children = {
           'a': TrieNode(
                  children = {
                    't': TrieNode(
                           children = {},
                           endOfWord = True
                         )
                  },
                  endOfWord = False
                )
         },
         endOfWord = False
       )
}
```

---

### Step-by-Step Construction in Code:

```python
cur = root  # TrieNode
cur.children = {'c': TrieNode}

cur = cur.children['c']
cur.children = {'a': TrieNode}

cur = cur.children['a']
cur.children = {'t': TrieNode(endOfWord=True)}
```

---

### Final Trie Structure:

```
root
 └─ 'c' → TrieNode
      └─ 'a' → TrieNode
           └─ 't' → TrieNode (endOfWord=True)
```

Each character is nested inside its parent character's `children` dictionary, forming a path from root to the last character of the word.
