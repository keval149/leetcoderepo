class Solution:
    def nonConstructibleChange(self,coins):
        # Write your code here.
        coins.sort()  # Sorting in-place

        changeCreated = 0

        for coin in coins:
            if coin > changeCreated + 1:
                return changeCreated + 1
            else:
                changeCreated = changeCreated + coin


        return changeCreated + 1

coins = [1,2,5]
obj = Solution()
result = obj.nonConstructibleChange(coins)
print("Non Constructible Change using the {} coins is {}".format(coins,result))

