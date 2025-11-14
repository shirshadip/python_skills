import tkinter as tk 
def say():
    print ("button clicked!")
root = tk.Tk()
root.title("buttons")
root.geometry("720x480")

btn = tk.Button(root,text="click here",command=say)
btn.pack(pady=50)

root.mainloop()