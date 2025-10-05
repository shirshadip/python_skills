#august 1,2025
#pascals triangle II
class solution (object):
    def getRow (self,rowIndex):
        row =[1]
        for i in range (1,rowIndex+1):
            new_row = [1]
            for j in range (1,len(row)):
                new_row.append (row [j-1]+row[j])
            new_row.append(1)
            row = new_row
        return row 
# Example usage:
sol = solution()
print(sol.getRow(int(input("enter the number of row:"))))  # Output: [1, 3, 3, 1]
print(sol.getRow(0))  # Output: [1]
print(sol.getRow(1))  # Output: [1, 1]