class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for i in nums:
            if i==0:
                red = red+1
            elif i==1:
                white = white+1
            elif i==2:
                blue = blue+1
        
        print(red, white, blue)
        
        pointer = 0
        while pointer<len(nums):
            if pointer<red:
                nums[pointer]=0
            elif pointer<red+white:
                nums[pointer]=1
            else:
                nums[pointer]=2
            pointer = pointer+1