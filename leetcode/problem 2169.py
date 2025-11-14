class Solution:
    def countOperations(self, num1: int, num2: int):
        c= 0 
        while num1 !=0 and num2 !=0:
            if num1 >= num2:
                num1 -= num2 
            else :
                num2-=num1 
            c +=1 
        return c     
s= Solution()
print (s.countOperations(5,4))