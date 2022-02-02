class Solution:
    def twoSum(self, nums: list[int], target: int)-> list[int]:
        if target == None:
            return None
        if nums == None or len(nums) <2:
            return None

        hmap = {}
        result = []

        for i in range(0,len(nums)):
            diff =  target - nums[i]
            if diff in hmap:
                result.append(hmap[diff])
                result.append(i)
                return result
            else:
                hmap[nums[i]] = i
        return result



obj = Solution()
list = [2,7,11,15]
target = 9
result = obj.twoSum(list,target)
print("Output is: {}".format(result))


'''
Output is: [0, 1]
Time Complexity: O(N) where N is the length of nums
Space Complexity: O(N) where N is the length of nums
'''