import tkinter as tk 

root = tk.Tk()
root.title("grid example")
root.geometry("720x480")
def clicked():
    print("Button clicked")
tk.Label(root,text="username",font=("Arial",16)).grid(row=0,column=0)
tk.Entry(root,font=("Arial",16)).grid(row=0,column=1)

tk.Button(root,text="submit",command=clicked).grid(row=1,column=0)
root.mainloop()