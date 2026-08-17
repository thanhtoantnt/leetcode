class Codec:
    """Encode a list of strings into one string and decode it back.

    Length-prefix framing: "len:#chunk" per string — the header is
    self-delimiting, so any payload (including #, colons, unicode) is
    safe. O(total bytes) both ways.
    """

    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        out = []
        i = 0
        while i < len(s):
            j = s.index(":", i)
            length = int(s[i:j])
            out.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return out


if __name__ == "__main__":
    strs = ["hello", "world:", "3:#nested", "", "ünïcode"]
    assert Codec().decode(Codec().encode(strs)) == strs
    print("ok")
