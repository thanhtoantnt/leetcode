from typing import List


class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.word: str | None = None  # set at word end


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """All dictionary words traceable in the grid (adjacent cells,
        no reuse). Trie + backtracking: the trie prunes dead prefixes,
        so a failed letter match never re-descends.

        O(m·n·4·3^(L−1)) worst case; the trie's early exits dominate.
        """
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        m, n = len(board), len(board[0])
        out: list[str] = []

        def dfs(r: int, c: int, node: TrieNode) -> None:
            ch = board[r][c]
            nxt = node.children.get(ch)
            if not nxt:
                return
            if nxt.word:
                out.append(nxt.word)
                nxt.word = None  # report once
            board[r][c] = "#"
            if r > 0:
                dfs(r - 1, c, nxt)
            if r < m - 1:
                dfs(r + 1, c, nxt)
            if c > 0:
                dfs(r, c - 1, nxt)
            if c < n - 1:
                dfs(r, c + 1, nxt)
            board[r][c] = ch

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)
        return out


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    assert sorted(Solution().findWords(board, words)) == ["eat", "oath"]
    print("ok")
