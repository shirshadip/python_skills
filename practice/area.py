class solution:
    def circle(self,pi,r):
        return pi*r**2
    def rect(self,l,b):
        return l*b
    def square(self,l):
        return l**2
sol= solution()
print(sol.circle(22/7,int (input ("enter radius value:"))))
print(sol.rect(int (input ("enter length value:")),int (input ("enter breadth value:"))))
print(sol.square(int (input ("enter side value:"))))