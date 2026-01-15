def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0:
        return 0
    maximum = 1
    seen = set()
    curr = 0
    for i in range(len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            while s[curr] != s[i]:
                seen.remove(s[curr])
                curr += 1
            curr += 1
            seen.add(s[curr])
        maximum = max(i - curr + 1, maximum)
    return maximum
