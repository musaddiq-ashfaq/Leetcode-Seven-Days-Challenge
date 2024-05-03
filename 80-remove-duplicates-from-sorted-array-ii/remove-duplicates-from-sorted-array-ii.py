class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        i = 1  
        count = 1  
        for j in range(1, n):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1  
            if count <= 2:
                nums[i] = nums[j]
                i += 1
        nums = nums[:i]
        return len(nums)