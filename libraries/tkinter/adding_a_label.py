import tkinter as tk 

root =tk.Tk()

root.title("adding a label")

#creating a label 
root.geometry("720x480")

label = tk.Label(root,text="Hello, Tkinter!")
label.pack(pady = 10)

root.mainloop()