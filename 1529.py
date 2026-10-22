class Solution:
    def minFlips(self, target: str) -> int:
        
        cnt = 0
        changes = 0
        state = 0
        for i, sub in enumerate(target):
            cur = ord(sub) - ord("0")
            if ( cur != state):
                state = cur
                cnt += 1
        return cnt
