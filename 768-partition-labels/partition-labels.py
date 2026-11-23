class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        start, end = 0, 0
        res = []

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                res.append(end-start+1)
                start = i+1
        return res
