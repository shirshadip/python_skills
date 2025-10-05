import pandas as pd 
data = {
    "name":["shirshadip","shreya","priyanka","ram","shyam","jodu","modhu"],
    "age":[32,34,35,36,37,38,39],
    "marks":[346,356,356,366,376,386,396]
}

df = pd.DataFrame(data)
print(df)
 

#view dataframe details

print (df.head())#display the first five rows
print (df.tail())#display the last five rows
print (df.shape)#(rows, columns)
print (df.columns)#list all columns
print (df.info())#summary of the dataframe
print (df.describe())#statistical summary of the dataframe
print (df["name"])  # Access the 'name' column