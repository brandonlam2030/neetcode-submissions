class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        r = 1
        word = [s[0]]
        maxi = 1

        while r < len(s):
            while s[r] in word:
                word.pop(0)
            word.append(s[r])
            maxi = max(maxi,len(word))
            r+=1
        return maxi