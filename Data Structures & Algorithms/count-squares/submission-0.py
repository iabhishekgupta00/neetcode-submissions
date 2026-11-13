from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        res = 0

        for (x2, y2), count in self.ptsCount.items():

            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:

                res += (
                    count
                    * self.ptsCount.get((x1, y2), 0)
                    * self.ptsCount.get((x2, y1), 0)
                )

        return res