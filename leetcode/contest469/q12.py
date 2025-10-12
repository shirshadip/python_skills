from collections import Counter
nums=[1,2,2,3,3,3,3,4]
k=2
freq=Counter(nums)
tot=0
for key , values in freq.items():
        if values %k==0:
            tot+=values*key
print(tot) 