from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0 
        count = {}
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            diff = (r-l+1) - max(count.items(),key = lambda x: x[1])[1]
            if diff <= k:
                result = max(result, r-l+1)
            else:
                while diff > k:
                    count[s[l]]-=1
                    l+=1
                    diff = (r-l+1) - max(count.items(),key = lambda x: x[1])[1]

        return result
        