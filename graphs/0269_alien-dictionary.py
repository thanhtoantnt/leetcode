from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """Derive the alphabet order from a sorted word list (premium).

        First differing character pair (w1[i], w2[i]) gives an edge
        "w1[i] must come before w2[i]". Kahn's topological sort on the
        letter graph; a cycle (contradiction) → "". A prefix violation
        (abc before ab) → "".
        """
        adj = defaultdict(set)
        indeg = {c: 0 for w in words for c in w}
        for w1, w2 in zip(words, words[1:]):
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indeg[b] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""
        q = deque(c for c in indeg if indeg[c] == 0)
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for nxt in adj[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return "".join(out) if len(out) == len(indeg) else ""


if __name__ == "__main__":
    assert Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert Solution().alienOrder(["z", "x", "z"]) == ""
    print("ok")
