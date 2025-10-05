import tkinter as tk 
window = tk.Tk()
window.title("user form")
window.geometry("300x400")
#name label and entry
tk.Label(window , text= "name").grid (row =0, column = 0,padx = 10, pady = 10)
name_entry= tk.Entry(window )
name_entry.grid (row = 0 , column =1 )
#gender radio buttons 
tk.Label(window, text="gender").grid(row=1,column=0)

gender =tk.StringVar()
tk.Radiobutton(window,text="male",variable=gender,value ="male").grid (row = 1 , column =1 , sticky = "w")
tk.Radiobutton(window ,text ="female",variable=gender,value="female").grid(row = 2 , column = 1 , sticky = "w")

#submit button 
def submit():
    print ("name" , name_entry.get())
    print ("gender", gender.get())

tk.Button (window, text ="submit",
command = submit).grid (row = 3 , column=1, pady = 10)

window.mainloop()