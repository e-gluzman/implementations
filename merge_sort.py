class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.merge_sort(nums)
        
    def merge_sort(self,nums):

        length = len(nums)
        
        if length <= 1:
            return nums
        
        midpoint = length//2
        
        #left = merge_sort(nums[:midpoint])
        
        #right = merge_sort(nums[midpoint:])
        
        #sorted_values = []
        
        left = nums[:midpoint]
        right = nums[midpoint:]
        
        self.merge_sort(left)
        self.merge_sort(right)
        
        l_index = 0
        r_index = 0
        nums_index = 0
        
        while l_index < len(left) and r_index < len(right):
            
            if left[l_index] < right[r_index]:
                
                #sorted_values.append(left[l_index])
                nums[nums_index] = left[l_index]
                
                l_index += 1
                
            else: 
                
                #sorted_values.append(right[r_index])
                nums[nums_index] = right[r_index]
                
                r_index += 1
                
            nums_index += 1
                
        while l_index < len(left):
            
            nums[nums_index] = left[l_index]
            
            l_index += 1
            nums_index += 1
        
        while r_index < len(right):
            
            nums[nums_index] = right[r_index]
            
            r_index += 1
            nums_index += 1
            
        #sorted_values += right[r_index:]
        #sorted_values += left[l_index:]
                    
        #return nums
        
