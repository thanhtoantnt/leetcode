from collections import Counter


class DetectSquares:
    """Count axis-aligned squares containing a query point.

    Points + a count map; for a query p, every stored diagonal point
    (x,y) with |x−px| = |y−py| > 0 fixes a square — the other two
    corners are (x, py) and (px, y), looked up by count. add O(1),
    count O(n).
    """

    def __init__(self):
        self.points: list[tuple[int, int]] = []
        self.cnt: Counter[tuple[int, int]] = Counter()

    def add(self, point: list[int]) -> None:
        p = (point[0], point[1])
        self.points.append(p)
        self.cnt[p] += 1

    def count(self, point: list[int]) -> int:
        px, py = point
        total = 0
        for x, y in self.points:
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue  # not a diagonal, or degenerate
            total += self.cnt[(x, py)] * self.cnt[(px, y)]
        return total


if __name__ == "__main__":
    d = DetectSquares()
    d.add([3, 10]); d.add([11, 2]); d.add([3, 2])
    assert d.count([11, 10]) == 1  # corners (3,10),(11,2),(3,2)
    assert d.count([14, 8]) == 0
    d.add([11, 2])
    assert d.count([11, 10]) == 2  # duplicate diagonal doubles
    print("ok")
