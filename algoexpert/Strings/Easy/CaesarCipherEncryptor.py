class Solution:

    def caesarCipherEncryptor(self,string, key):
        # Write your code here.
        key = key % 26
        result = ""
        for ch in string:
            ascii_value = (ord(ch) + key)
            if ascii_value > 122:
                ascii_value = ascii_value - 26
            new_char = chr(ascii_value)
            result = result + new_char


        return result

string = "xyz"
key = 2
obj = Solution()
result = obj.caesarCipherEncryptor(string,key)
print(" The Caesar Cipher Encryptor of {} with  key={} is {} ".format(string,key,result))