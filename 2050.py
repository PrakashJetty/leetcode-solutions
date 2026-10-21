class Solution:
  
    def __init__(self):
        self.adjDict = {}
        self.dp = []

    def minimumTimeForNode(self, node : int, time : list[int]) -> int:
        if self.dp[node] != 0:
            return self.dp[node]        
        else:
            res = time[node - 1]
            max_time = 0
            for rel in self.adjDict[node]:
                max_time = max(max_time, self.minimumTimeForNode(rel, time))
            res += max_time
            self.dp[node] = res
            # print(f"node = {node}, {res}")
            return res

    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        self.dp = [0] * (n + 1)
        for idx, re in enumerate(relations):
            inv , outv = re[0], re[1]
            if outv not in self.adjDict:
                self.adjDict[outv] = []
                #end_nodes.add(outv)
            self.adjDict[outv].append(inv)
        ans = 0
        for node in range(1, n + 1):
            if node not in self.adjDict:
                self.dp[node] = time[node - 1]
        for node in range(1, n + 1):
            if node not in self.adjDict:
                ans = max(ans, self.dp[node])
            else:
                ans = max(ans, self.minimumTimeForNode(node, time))
            print(f"node = {node}, {ans}")
        return ans
