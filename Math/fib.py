class Solution:
    def __init__(self, d : dict)-> None:
        self.map = d

    def fib(self, n: int)-> int:
        if n in self.map:
            return self.map[n]
        self.map[n] = self.fib(n-1) + self.fib(n-2)
        return self.map[n]



n = 10
d = {0:0,1:1}
obj = Solution(d)
res = obj.fib(n)
print("The fibonnaci output of n = {} is {}".format(n,res))


'''
The fibonnaci output of n = 10 is 55
Time Complexity : O(N)
Space Complexity: O(N)
'''

