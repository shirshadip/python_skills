import torch 
#check device cpu or gpu
device = "cuda" if torch.cuda.is_available() else "cpu"
print ("using device",device)

#creates tensors 
a = torch.tensor([1,2,3],dtype=torch.float32)
b = torch.tensor([4, 5, 6], dtype=torch.float32)

print ("tensor a :",a)
print ("tensor b :",b)
