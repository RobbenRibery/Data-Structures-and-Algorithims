class Solution(object):
    def minSubArrayLen_two_pointers(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum_ = 0 
        j = 0 
        for i in range(len(nums)): 
            
            sum_ += nums[i]
            
            if sum_ >= target: 
                
                if j == 0:
                    res = i-j+1
                else:
                    res = min(res, i-j+1)
                
                while sum_ >= target: 
                    
                    res = min(res, i-j+1)
                    sum_ -= nums[j]
                    j += 1 
                
        return res

    def minSubArrayLen_binary_search(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum_ = 0 
        j = 0 
        for i in range(len(nums)): 
            
            sum_ += nums[i]
            
            if sum_ >= target: 
                
                if j == 0:
                    res = i-j+1
                else:
                    res = min(res, i-j+1)
                
                while sum_ >= target: 
                    
                    res = min(res, i-j+1)
                    sum_ -= nums[j]
                    j += 1 
                
        return res


if __name__ == "__main__": 

    sol = Solution()

    print(sol.minSubArrayLen_two_pointers(7,[2,3,1,2,4,3]))