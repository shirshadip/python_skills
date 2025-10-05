class student :
    def __init__(self,name, age,roll_no) -> None:
        #attributes (variables inside a class)
        self.name = name 
        self.age = age 
        self.roll_no = roll_no

    #method a function inside a class 
    def showinfo (self):
        print (f"name:{self.name}, age : {self.age}. roll_no. : {self.roll_no}")

#cerating objects 

student1 = student("john", 15, 101)
student2 = student("alice", 14, 102)

student1.showinfo()
student2.showinfo()