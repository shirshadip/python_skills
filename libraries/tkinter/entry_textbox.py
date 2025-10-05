import tkinter as tk 
def show():
    user_text=entry.get()
    print("You entered:", user_text)

root = tk.Tk()
entry = tk.Entry(root,font=("Arial",16))
entry.pack()
root.title("entry example")
root.geometry("720x480")

label= tk.Label(root,text="click the button",font=("Arial",16))
label.pack(pady=20)

button= tk.Button(root,text="submit",command=show)
button.pack(pady=20)


label=tk.Label(root,text="",font=("Arial",16))
label.pack(pady=20)

root.mainloop()