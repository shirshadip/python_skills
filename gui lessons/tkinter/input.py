import tkinter as tk 
def show_name ():
    print("your name is:",entry.get())
root = tk.Tk()
entry=tk.Entry(root,width=30)
entry.pack(pady=10)

btn = tk.Button(root,text="submit",command=show_name)
btn.pack()
root.mainloop()