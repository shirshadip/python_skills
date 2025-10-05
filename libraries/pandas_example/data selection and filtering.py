import pandas as pd 

data = {
    "name":["shirsha","shreya","priyanka"],
    "age":[32,34,43],
    "marks":[85,90,78]
}
df = pd.DataFrame(data)
print(df)

print (df["marks"]) #access "marks"