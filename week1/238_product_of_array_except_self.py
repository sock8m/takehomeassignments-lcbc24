class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix = list(nums)
        suffix = list(nums)
        answer = list()

        i = 1
        j = len(nums)-2

        # creating prefix array
        while i<len(nums):
            prefix[i] = prefix[i]*prefix[i-1]
            i = i+1
        
        print(prefix)
        
        # creating suffix array
        while j>-1:
            print(suffix[j])
            suffix[j] = suffix[j]*suffix[j+1]
            j = j-1

        print(suffix)
        
        for k in range(len(nums)):
            if k==0:
                answer.append(suffix[k+1])
            elif k==len(nums)-1:
                answer.append(prefix[k-1])
            else:
                answer.append(prefix[k-1]*suffix[k+1])

        return answer