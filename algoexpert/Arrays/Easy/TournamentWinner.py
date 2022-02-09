class Solution:
    def tournamentWinner(self,competitions:list[list[str]], results:list[int])-> str:
        # Write your code here.
        # winner = 0
        d = {}
        win_count = 0
        winteam = ""
        for i in range(0, len(results)):
            # print(i)
            # print(results[i])
            if (results[i] == 0):
                d[competitions[i][1]] = d.get(competitions[i][1], 0) + 1
            # winner = max(d[competitions[i][1]],winner)

            else:
                d[competitions[i][0]] = d.get(competitions[i][0], 0) + 1
            # winner = max(d[competitions[i][0]],winner)

        for key in d:
            if (d[key] > win_count):
                winteam = key
                win_count = d[key]
        # print(winner)
        return winteam

competitions = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
results = [0,0,1]
obj =  Solution()
result = obj.tournamentWinner(competitions,results)
print("Winning team is: {}".format(result))


