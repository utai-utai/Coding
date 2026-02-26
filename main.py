from typing import List

class Solution:
    def aaa(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(sub) -> bool:
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        def backtrack(startIndex: int):
            if startIndex == len(s):
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                if isPalindrome(s[startIndex:i]):
                    path.append(s[startIndex:i])
                    backtrack(i+1)
                    path.pop()

        backtrack(0)
        return res