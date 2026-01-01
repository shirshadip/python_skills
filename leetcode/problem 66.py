class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=""
        for i in digits:
            d += str (i)
        num = int (d)
        nnum= num+1
        innum= str (nnum)
        newarr=[]
        for j in innum:
            newarr.append(int(j))
        return newarr
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9]))