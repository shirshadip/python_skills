import pandas as pd 
data = {
    "name":["shirshadip","shreya","priyanka"],
    "age":[32,34,35],
    "marks":[346,356,356]
}

df = pd.DataFrame(data)
print(df)
 

 #explore dataframe 
print(df.head())  # Display the first five rows of the DataFrame
print(df.describe())  # Get a statistical summary of the DataFrame
print(df.columns) # List all the columns in the DataFrame
print(df["name"])  # Access the 'name' column

