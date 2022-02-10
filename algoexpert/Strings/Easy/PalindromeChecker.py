class Solution:
    def isPalindrome(self,string):
        # Write your code here.
        left = 0
        right = len(string)-1
        while(left <= right):
            if string[left] == string[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True

string = "madam"
obj = Solution()
result = obj.isPalindrome(string)
print("Is {} a Palindrome : {}".format(string,result))