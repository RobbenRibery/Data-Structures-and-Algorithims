class Solution(object): 

    def productExceptSelf(self, nums): 

        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        
        res = []


        return res 


if __name__ == '__main__': 

    nums = [1,2,3,4]

    # 1 - 2 * 3 * 4 
    # 2 - 1 * 3 * 4 
    # 3 - 1 * 2 * 4 
    # 4 - 1 * 2 * 3 

    sol = Solution

    print(sol.productExceptSelf(nums))