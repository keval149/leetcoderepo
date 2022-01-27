class reverseString:
    def __init__(self, s: list, start: int, stop: int) -> None:
        self.lstr = s
        self.left = start
        self.right = stop
        self.length = len(s)-1


    def reverseStringbetween(self) -> list:
        while(self.left < self.right):
            self.lstr[self.left], self.lstr[self.right] = self.lstr[self.right], self.lstr[self.left]
            self.left = self.left + 1
            self.right = self.right - 1

        return self.lstr

inp = ["This", "is", "a", "new", "pen"]
j = 1
k = 3
obj = reverseString(inp,j,k)
print ("The original is {}".format(inp))
result = obj.reverseStringbetween()
print ("The reverse from {} to {} is {}".format(j,k,result))


'''
Output is : 
The original is ['This', 'is', 'a', 'new', 'pen']
The reverse from 1 to 3 is ['This', 'new', 'a', 'is', 'pen']
'''

'''
Time complexity : O(n)
Space complexity : O(1)
'''



