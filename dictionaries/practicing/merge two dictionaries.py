"""6️⃣ Problem: Merge Two Dictionaries

Task:

Merge {“a”: 1, “b”: 2} and {“b”: 3, “c”: 4}.

In case of duplicate keys, add their values."""
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}

merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key]+=value
    else :
        merged[key]=value

print ("merged dictionary:",merged)