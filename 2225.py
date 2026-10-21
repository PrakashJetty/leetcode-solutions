class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        lost = {}
        lost_once = list()
        won = set()
        won_all = list()
        for game in matches:
            winner, loser = game[0], game[1]
            if loser in lost:
                lost[loser] += 1
            else:
                lost[loser] = 1
            won.add(winner)
        for can in won:
            if can not in lost:
                won_all.append(can)
        for can, times in lost.items():
            if times == 1:
                lost_once.append(can)
        won_all.sort()
        lost_once.sort()

        return [won_all, lost_once]

        
