class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.end = False


class Trie:
    """Prefix tree: insert/search/startsWith, all O(L) in word length.

    Each node is a 26-way map layer; a word's path spells it, and the
    'end' flag separates stored words from bare prefixes.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def _walk(self, s: str) -> TrieNode | None:
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if not node:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.end)

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.startsWith("app")
    t.insert("app")
    assert t.search("app")
    print("ok")
