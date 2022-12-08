from typing import List
import collections 
class Solution:
    def dailyTemperatures_idea1(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)
        max_deque = []

        # assemble the maximum list 
        max_r = [30]*(len(temperatures)-1) + [temperatures[-1]]
        for i in range(len(temperatures)-1,-1,-1):
            if i != len(temperatures)-1:
                max_r[i] = max(temperatures[i],max_r[i+1])

        # iterate again to calculate the waiting peroid based on max deque 
        for i in range(len(temperatures)): 
            print(f"Loop{temperatures[i]}")
            
            if max_deque: 
                while max_deque and temperatures[i] >= max_deque[-1][0]: 
                    print('in')
                    if temperatures[i] > max_deque[-1][0]:
                        res[max_deque[-1][1]] += 1 
                        max_deque.pop()
                    else: 
                        if temperatures[i] < max_r[i]: 
                            #res[max_deque[-1][1]] += 1 
                            break 
                        else: 
                            max_deque.pop()
                            print(max_deque)
                     
                #print(res)
                #print(max_r)

                for j in range(len(max_deque)):
                    if max_deque[j][0] < max_r[max_deque[j][1]]: 
                        #print(max_deque[j][0],max_r[max_deque[j][1]])
                        #print(res)
                        res[max_deque[j][1]] += 1 
                        #print(res)
        

                print(res)
            
            max_deque.append([temperatures[i],i])
            #print(max_deque)
            #print()

        return res
            

if __name__ == "__main__": 

    temperatures = [71]*4
    #temperatures = [34,80,80,34,34,80,80,80,80,34]
    #temperatures = [30,40,50,60]
    #temperatures = [30, 60, 90]

    sol = Solution()

    print(sol.dailyTemperatures_idea1(temperatures))