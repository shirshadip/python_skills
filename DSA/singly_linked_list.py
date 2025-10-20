class node :
    def __init__(self,data):
        self.data = data #store  data 
        self.next=None #pointer to the next node 
#linked list class 
class linkedlist :
    def __init__(self) -> None:
        self.head=None #initially empty list 
    def apppend (self,data): #method to add new node at the end 
        new_node = node(data)
        if self.head is None: #if list is empty 
            self.head= new_node
            return
        current =self.head
        while current.next: #traverse to last node 
            current = current.next
        current.next= new_node
    #method to print the linked list 
    def disply (self):
        current = self.head 
        while current:
            print (current.data,end="->")
            current=current.next
        print ("none")
#usage 
li= linkedlist()
li.apppend(10)
li.apppend(20)
li.apppend(30)
li.disply()