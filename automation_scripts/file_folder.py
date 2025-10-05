import os

folder_path = r"d:\python\automation_scripts\random"

for filename in os.listdir(folder_path):
    print("Checking:", filename)  # Debug

    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path, filename)
        new_filename = filename.replace(".txt", "_new.txt")
        new_path = os.path.join(folder_path, new_filename)

        print(f"Renaming {old_path} -> {new_path}")  # Debug
        os.rename(old_path, new_path)
