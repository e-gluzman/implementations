class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort

        length = len(nums)
        
        for i in range(length):
            
            for j in range(0,length-i-1):
                
                if nums[j] > nums[j+1]:
                    
                    nums[j], nums[j+1] = nums[j+1],nums[j]
                    
        return nums
