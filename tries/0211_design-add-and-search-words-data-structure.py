class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.end = False


class WordDictionary:
    """Trie + DFS over wildcards: '.' matches any letter.

    search walks the trie; on '.', fan out to every child (each '.'
    multiplies work by ≤26, but only along existing paths).
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return bool(child) and dfs(child, i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":
    d = WordDictionary()
    d.addWord("bad")
    d.addWord("dad")
    d.addWord("mad")
    assert not d.search("pad")
    assert d.search("bad")
    assert d.search(".ad")
    assert d.search("b..")
    print("ok")
