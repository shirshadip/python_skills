import tkinter as tk 

def say_hello():
    print("Hello, Tkinter!")

root = tk.Tk()
root.title("button example")
root.geometry("720x480")

label = tk.Label(root, text="click the button", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="click here", command=say_hello)
button.pack(pady=10)

root.mainloop()