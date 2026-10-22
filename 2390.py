class Solution:
    def removeStars(self, s: str) -> str:
        subs = []
        for sub in s:
            if sub != "*":
                subs.append(sub)
            else:
                if subs:
                    subs.pop()
        return "".join(subs)
