class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            if nums[i]>nums[i+1]:
                temp=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
            else:
                if i<len(nums)-1:
                    i = i+1
                else:
                    return