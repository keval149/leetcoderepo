class Solution:
    def __init__(self, steps:dict)-> None:
        self.steps = steps


    def climbStairs(self, n: int) -> int:
        if n in self.steps:
            return self.steps[n]
        self.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.steps[n]

d = {1:1,2:2}
n = 5
obj = Solution(d)
result = obj.climbStairs(n)
print("Number of different ways to climb {} stairs is {}".format(n,result))


'''
Output:
Number of different ways to climb 5 stairs is 8

Time Complexity: O(N)
Space Complexity: O(N)
'''