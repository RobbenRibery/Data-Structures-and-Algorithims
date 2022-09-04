from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums:list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) > 0:
            
            # result to be returned
            history_max_res = 1 

            # temp result for each chain 
            res = 1  
            
            # bulid the dictionary {num: count of occurence} O(n)
            occurence_map = defaultdict(int)
            for num in nums:
                occurence_map[num] += 1 

            # iterate through the list O(n)
            for num in nums: 
                
                # if res = 1, no value has been added on chain, 
                # rest the left_query and right_query according to the new value 
                if res == 1: 

                    left_query = num - 1
                    right_query = num + 1

                if occurence_map[left_query] != 0 or occurence_map[right_query] != 0: 
                    
                    # if digits on left hand side on chain 
                    if occurence_map[left_query] != 0 and occurence_map[right_query] == 0: 

                        res += 1 
                        occurence_map[left_query] -= 1 
                        left_query -= 1 

                    # if digits on right side on chain, 
                    # or both digits on chain, default going to right hand-side 
                    else: 
                        res += 1 
                        occurence_map[right_query] -= 1 
                        right_query += 1 

                else: 
                    # the chain is broken at this point 

                    # if res(count) equals to one, 
                    if res > 1: 
                        if res > history_max_res: 
                            history_max_res = res 

                        res = 1

            return history_max_res

        else: 
            return 0

if __name__ == '__main__': 

    nums_1 = [100,4,200,1,3,2]
    nums_2 = [0,3,7,2,5,8,4,6,0,1]
    nums_3 = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    nums_4 = []
    nums_5 = [0]


    solution = Solution()

    print(solution.longestConsecutive(nums_1))
    print(solution.longestConsecutive(nums_2))
    print(solution.longestConsecutive(nums_3))
    print(solution.longestConsecutive(nums_4))
    print(solution.longestConsecutive(nums_5))







            

        
            
           