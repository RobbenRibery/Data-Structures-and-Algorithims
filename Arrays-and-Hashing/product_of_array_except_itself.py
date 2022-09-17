def productExceptSelf(nums): 

    """
    :type nums: List[int]
    :rtype: List[int]
    :solution must be provided without using divsion method 

    Solution: 
    - Go through the entire array from 

    Complexity: 
    - N = len(nums)
    - TC: 0(N)
    - SC: 0(N) / 0(1) if discount the output aray 
    """ 
    res = [1]*len(nums)

    # left propogation 
    for i in range(1,len(nums)): 
        res[i] = res[i-1] * nums[i-1]

    # right propogation 
    right_prod = nums[-1]
    for i in range(len(nums)-2, -1, -1): 

        res[i] *= right_prod
        right_prod *= nums[i] 

    return res 


if __name__ == '__main__': 

    nums_1 = [1,2,3,4]
    nums_2 = [-1,1,0,-3,3]
    # - if 
    ## one position is zero, the rest of positions are all zero 

    # - else
    ## 1 - 2 * 3 * 4 * 0
    ## 2 - 1 * 3 * 4 * 0
    ## 4 - 1 * 2 * 3 * 0
    ## 3 - 1 * 2 * 4 * 0
    ## 0 - 1 * 2 * 3 * 4 
    print(productExceptSelf(nums_1))
    print(productExceptSelf(nums_2))

    ## left to write pass

    # i: 0-> len(nums)

    ## i = 0 -> lhs[i] *= 1 
    ## i = 1 -> lhs[i] = lhs[i-1] * nums[i-1]


    ### lhs = [1,1,2,6]

    # 3 -> 2 * 4 
    # 2 -> 1 res[i] * 3 nums[i-1] * 4 nums[i-1]
     


    ## right to left pass 

    # i: len(nums)-1 -> 0 
    ## i = len(nums) -1 -> lhs[i] *= 1 
    ## i = len(nums) -2 -> lhs[i] = lhs[i+1] * nums[i+1]


    # return lhs 





