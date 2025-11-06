# src/trie.py
"""
Trie data structure for autocomplete.

Public surface expected by tests:
- class Trie
  - insert(word: str, freq: float) -> None
  - remove(word: str) -> bool
  - contains(word: str) -> bool
  - complete(prefix: str, k: int) -> list[str]
  - stats() -> tuple[int, int, int]  # (words, height, nodes)

Complexity target (justify in docstrings):
- insert/remove/contains: O(len(word))
- complete(prefix, k): roughly O(m + k log k')
"""

class TrieNode:
    __slots__ = ("children", "is_word", "freq")

    def __init__(self):
        self.children = {}
        self.is_word = False
        self.freq = 0.0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._words = 0
        self._nodes = 1

    def insert(self, word, freq):
        if not word:  # handle empty string
            return
        
        word = word.lower()  # normalize case
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                self._nodes += 1
            node = node.children[ch]
            
        if not node.is_word:
            node.is_word = True
            self._words += 1
        node.freq = float(freq)

    def remove(self, word):
        if not word:  # handle empty string
            return False
            
        word = word.lower()  # normalize case
        node = self.root
        stack = []  # nodes along path
        for ch in word:
            if ch not in node.children:
                return False
            stack.append((ch, node))
            node = node.children[ch]
        if not node.is_word:
            return False
        # unset word
        node.is_word = False
        node.freq = 0.0
        self._words -= 1
        # prune nodes if they have no children and are not word
        for ch, parent in reversed(stack):
            child = parent.children[ch]
            if child.children or child.is_word:
                break
            del parent.children[ch]
            self._nodes -= 1
        return True

    def contains(self, word):
        if not word:  # handle empty string
            return False
            
        word = word.lower()  # normalize case
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def complete(self, prefix, k):
        # sanitize inputs
        if prefix is None:
            prefix = ''
        # normalize case so callers can use upper/lower case prefixes
        prefix = prefix.lower()
        try:
            k = int(k)
        except Exception:
            # invalid k -> no results
            return []
        if k <= 0:
            return []

        # find start node
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []

        def dfs(n, path):
            if n.is_word:
                results.append((path, n.freq))
            for c in n.children:
                dfs(n.children[c], path + c)

        dfs(node, prefix)
        # sort by frequency desc, tie-break lexicographically
        results.sort(key=lambda x: (-x[1], x[0]))
        return [w for w, _ in results[:k]]

    def stats(self):
        # compute height (max depth of any node from root)
        max_depth = 0

        def dfs_depth(n, depth):
            nonlocal max_depth
            if depth > max_depth:
                max_depth = depth
            for c in n.children:
                dfs_depth(n.children[c], depth + 1)

        dfs_depth(self.root, 0)
        return (self._words, max_depth, self._nodes)

    def items(self):
        # iterate (word, freq) for all words in trie
        out = []

        def dfs(n, path):
            if n.is_word:
                out.append((path, n.freq))
            for c in n.children:
                dfs(n.children[c], path + c)

        dfs(self.root, '')
        return out
