import os

folder_path = r"d:\python\automation_scripts\random"

if os.path.exists(folder_path):
    print("✅ Folder exists:", folder_path)
    print("📂 Files inside:")
    for f in os.listdir(folder_path):
        print("  -", f)
else:
    print("❌ Folder not found!")
