import pandas as pd
marks = {
    "shirshadip": 346,
    "shreya": 356,
    "priyanka": 356
}

s = pd.Series(marks)
print(s)

#accesing data from series
print(s["shirshadip"])  # Accessing a specific value by index
print (s[0])#access data by position
print (s[0:2]) #access by slicing
print (s.index)  # Display the index of the Series