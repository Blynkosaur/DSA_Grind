class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert = 0
        hor = 0
        for s in moves:
            if s == "U":
                vert += 1
            elif s == "D":
                vert -= 1
            elif s == "L":
                hor -= 1
            else:
                hor += 1
        return hor == 0 and vert == 0