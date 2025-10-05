import os 
def oraganize_file_by_extension(folder_path):
    #go to the target folder
    os.chdir(folder_path)

    #lis all folders and files in the directory
    for item in os.listdir():
        if os.path.isfile(item): #only works with files
            file_name,file_ext =os.path.splitext(item)
            file_ext = file_ext[1:] #remove the dot

            if file_ext == "": #skips files with no extension
                continue

            #creat folder for extension if it doesn't exist
            if not os.path.exists(file_ext):
                os.mkdir(file_ext)

                #move file to its own folder
                os.rename(item,os.path.join(file_ext,item))

    print("Files organized by extension!")
#change this path to the folder you want to organize 
folder = str (input("enter the path of your folder: "))
oraganize_file_by_extension(folder)