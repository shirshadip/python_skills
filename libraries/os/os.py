import os

def os_operations():
    try:
        # Print current working directory
        print("Current Directory:", os.getcwd())

        # Change directory
        path = input("Enter the path to change directory: ")
        os.chdir(path)
        print("Directory changed to:", os.getcwd())

        # List contents of the current directory
        print("Contents of the directory:", os.listdir())

        # Create a new folder
        new_folder = input("Enter the name of new folder to create: ")
        os.mkdir(new_folder)
        print(f"Folder '{new_folder}' created.")

        # Create nested directories (main/sub)
        main_folder = input("Main folder name: ")
        sub_folder = input("Subfolder name: ")
        os.makedirs(os.path.join(main_folder, sub_folder))
        print(f"Nested folders '{main_folder}/{sub_folder}' created.")

        # Remove a folder (only if empty)
        folder_to_remove = input("Enter the name of the folder to remove: ")
        os.rmdir(folder_to_remove)
        print(f"Folder '{folder_to_remove}' removed.")

        # Remove nested directories (only if all are empty)
        main_remove = input("Main folder to remove: ")
        sub_remove = input("Subfolder to remove: ")
        os.removedirs(os.path.join(main_remove, sub_remove))
        print(f"Nested folders '{main_remove}/{sub_remove}' removed.")

        # Rename a file or folder
        old_name = input("Name of old file/folder: ")
        new_name = input("New name: ")
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")

        # Check if path exists
        path_check = input("Enter path to check if it exists: ")
        if os.path.exists(path_check):
            print("Path exists.")
        else:
            print("Path does not exist.")

        # Join folder and file name
        folder = input("Folder name: ")
        file = input("File name: ")
        full_path = os.path.join(folder, file)
        print("Joined path:", full_path)

    except Exception as e:
        print("Error:", e)

# Call the function
os_operations()
