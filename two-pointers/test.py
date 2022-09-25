nums = [-1,0,1,2,-1,-4]
left_index = 0
right_index = len(nums)-1

temp_nums = nums[:left_index] + nums[left_index+1:right_index] + nums[right_index+1:]

print(temp_nums)