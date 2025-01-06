class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ret = [0] * len(boxes)
        for box in range(len(boxes)):
            if boxes[box] == "1":
                for i in range(len(boxes)):
                    ret[i] += abs(box-i)
            else:
                continue
        return ret
