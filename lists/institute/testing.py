my_list = [1, 2, 3, 4, 2, 5]
seen = set()
has_duplicates = False

for item in my_list:
    if item in seen:
        has_duplicates = True
        break
    seen.add(item)

print("Duplicates found!" if has_duplicates else "No duplicates.")
