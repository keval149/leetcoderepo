class Solution:
    def fib(self, n: int)-> int:
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        return self.fib(n-1) + self.fib(n-2)

n = 5
obj = Solution()
res = obj.fib(n)
print("The fibonnaci output of n = {} is {}".format(n,res))


'''
The fibonnaci output of n = 5 is 5
Time Complexity : O(2^N)
Space Complexity: O(N)
'''

