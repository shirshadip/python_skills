from typing import List
# from collections import Counter as c
class Solution:
    def kLengthApart(self, nums: List[int], k: int):
       
        zc = 0 
        for e,i in enumerate(nums):
            # if i == 1:
            #     continue
            # else :
            #     zc += 1
            #     break;
            print (i);
            print ("itretion: ",e);
                
                
        
        
        
        
        # [1,0,0,0,1,0,0,1]zc = 0
        
s = Solution()
print (s.kLengthApart([1,0,0,0,1,0,0,1],2))