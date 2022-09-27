from audioop import maxpp
from turtle import left


class Solution(object):
    def trap_condense(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # find the left_start, max and right_start indedx 
        left_start = 0
        right_start = len(height)-1
        max_height = 0 
        max_i = 0
        
        # collect the maximum value (O(N))
        for i in range(len(height)): 
            if height[i] > max_height: 
                max_height = height[i]
                max_i = i 

        maxes =  [height[left_start], height[right_start]]
        resses = [
            height[left_start] * max((max_i-left_start-1),0), 
            height[right_start] * max((right_start-max_i-1),0)
            ]
        indexies = [left_start+1, right_start-1]

        while indexies[0] < max_i or indexies[1] > max_i:

            for i, index in enumerate(indexies): 

                if abs(max_i-index)>0:
                
                    if resses[i] != 0: 
                        resses[i] -= min(height[index], maxes[i])

                    resses[i] += max(0,(height[index]- maxes[i])) * (abs(max_i-index)-1)
                    maxes[i] = max(height[index],  maxes[i])
                    indexies[i] += 1 if index < max_i else -1 
   
        return sum(resses)

    def trap_submitted(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # find the left_start, max and right_start indedx 
        left_start = 0
        right_start = len(height)-1
        max_height = 0 
        max_i = 0
        
        # collect the last occurence of the maximum value from the list 
        # in the height list we can have multiple occurences of the 
        # maximum value 
        for i in range(len(height)): 
            if height[i] > max_height: 
                max_height = height[i]
                max_i = i 

        l_max = height[left_start]
        r_max = height[right_start]
        res_left = l_max * max((max_i-left_start-1),0)
        res_right =  r_max * max((right_start-max_i-1),0)

        left_start += 1 
        right_start -= 1 

        while left_start < max_i or right_start > max_i:
            
            if max_i > left_start:
                
                height_to_deduct_left = min(height[left_start], l_max)
                height_to_add_left = max(0,(height[left_start]-l_max))

                if res_left != 0:
                    res_left -= height_to_deduct_left 
                res_left += height_to_add_left * (max_i-left_start-1)

                l_max = max(height[left_start], l_max)
                left_start += 1

            if max_i < right_start:

                height_to_deduct_right = min(height[right_start], r_max)
                height_to_add_right = max(0,(height[right_start]-r_max))

                if res_right != 0:
                    res_right -= height_to_deduct_right 
                res_right += height_to_add_right *  (right_start-max_i-1)

                r_max = max(height[right_start], r_max)
                right_start -= 1 

        return res_left + res_right

if __name__ == '__main__': 

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    res = sol.trap_condense(height=height)
    print()
    print(res)


    height_1 = [4,2,0,3,2,5]
    sol = Solution()
    res_1 = sol.trap_condense(height=height_1)
    print()
    print(res_1)

    height_2 = [5,4,1,2]
    sol = Solution()
    res_2 = sol.trap_condense(height=height_2)
    print()
    print(res_2)



        
