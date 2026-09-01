# Tries

## Core idea

Prefix tree: one node per character, path from root spells a prefix. Insert/search O(L) in word length, independent of dictionary size. Shines when many words share prefixes or you need prefix queries / wildcard matching / multi-word search over a grid.

## Recognition signals

- "startsWith / autocomplete / prefix count" -> trie
- "Search with wildcard ." -> trie + DFS branching at the dot
- "Find MANY words in a grid at once" -> trie of words + one grid DFS (Word Search II)

## Templates

```python
class TrieNode:
    def __init__(self):
        self.children = {}          # char -> TrieNode
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.end = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for c in s:
            node = node.children.get(c)
            if node is None:
                return None
        return node

# wildcard search: DFS, branch on "."
def search(node, i, word):
    if i == len(word):
        return node.end
    c = word[i]
    if c == ".":
        return any(search(ch, i + 1, word) for ch in node.children.values())
    return c in node.children and search(node.children[c], i + 1, word)
```

Word Search II: build trie of all words, DFS the grid following trie edges only; record at end-nodes, prune (delete) exhausted leaves for speed.

## Complexity

Insert/search/prefix O(L). Space O(total chars * children map). Wildcard worst case branches to O(26^dots).

## Pitfalls

- setdefault keeps insert to one line - know it.
- Mark word ends explicitly; a prefix existing is NOT the word existing.
- Word Search II without trie (per-word DFS) times out - the trie sharing is the point.
- Deduplicate found words (set) or unmark end flag after recording.
