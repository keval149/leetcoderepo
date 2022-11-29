class Solution:
    def threeSum(self,nums:list[int])->list[list[int]]:

        # Soring the input nums array as to handle the duplicate results
        nums.sort()
        result = []
        temp = []
        hmap = {}

        # Inserting into hmap the indexes of the items in num
        for index in range(0,len(nums)):
            hmap[nums[index]] = index

        '''
        i is the pointer to the first element and j is the pointer to the element after i
        so j will be begin from i+1
        diff is the value that we look for to achieve nums[i] + nums[j] + diff  = 0
        So diff has to be after j , because we don't want to consider same element that appeared before j that could result in same output 
         
        '''
        print(nums)
        #ptr =0
        #for i in range(0,len(nums)-2):
        i = 0
        while (i < len(nums)-2):
            print("for loop i value is: {}".format(i))
            for j in range(i+1,len(nums)-1):
                print("second for loop i value is: {}".format(i))
                diff = 0 - nums[i] - nums[j]
                if diff in hmap and hmap[diff] > j:
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(diff)
                    result.append(temp)
                    temp = []
                i = hmap[nums[i]]

                print("hasmap i value is: {}".format(i))
                # this is done to avoid repeating duplicate values to be considered again and keeping result unique like [-1,-1,-1,....]
                j = hmap[nums[j]]

                # same as above

        return result


obj = Solution()
arr = [-1,0,1,2,-1,-4]
result = obj.threeSum(arr)
print("Output is : {}".format(result))
